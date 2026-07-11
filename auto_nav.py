#!/usr/bin/env python3
"""
Auto-sync mkdocs.yml nav section with docs/ directory changes.

当 docs/ 目录下有 .md 文件或文件夹被创建/删除时，
自动在 mkdocs.yml 的 nav 区域同步更新。

Usage:
    python3 auto_nav.py              # 一次性扫描 docs/ 并更新 nav
    python3 auto_nav.py --watch      # 持续监控 docs/ 变化（轮询模式）
    python3 auto_nav.py --watch -i 3 # 每 3 秒检查一次
    python3 auto_nav.py --dry-run    # 仅打印变更，不写入文件
"""

import os
import re
import sys
import time
import argparse
import shutil
from pathlib import Path
from typing import Optional
from collections import defaultdict

# ---------------------------------------------------------------------------
# 路径配置
# ---------------------------------------------------------------------------
DOCS_DIR = Path(__file__).resolve().parent / "docs"
MKCONFIG = Path(__file__).resolve().parent / "mkdocs.yml"

# 不需要加入 nav 的目录（资源目录等）
SKIP_DIRS = {"src", "res", "attachment", "assets", "__pycache__",
             ".obsidian", ".git", "images", "image"}

# 不需要加入 nav 的文件模式
SKIP_FILES = {".DS_Store", "README.md"}

# 占位文件：nav 中引用但实际上不存在的文件，同步时不删除
PLACEHOLDER_FILES = {"none.md", "1.md"}

# ---------------------------------------------------------------------------
# 数据结构：Nav 节点
# ---------------------------------------------------------------------------
class NavNode:
    """表示 nav 中的一个条目（章节标题 或 文件引用）。"""
    def __init__(self, display: Optional[str] = None,
                 path: Optional[str] = None,
                 indent: int = 0):
        self.display = display      # 显示名称 (None 表示裸路径如 - path.md)
        self.path = path            # md 文件相对路径 (None 表示这是章节)
        self.indent = indent        # 缩进空格数
        self.children: list[NavNode] = []
        self.parent: Optional[NavNode] = None

    @property
    def is_section(self) -> bool:
        return self.path is None and self.display is not None

    @property
    def is_named_leaf(self) -> bool:
        return self.path is not None and self.display is not None

    @property
    def is_bare_leaf(self) -> bool:
        return self.path is not None and self.display is None

    def __repr__(self):
        if self.is_section:
            return f"Section({self.display!r}, children={len(self.children)})"
        elif self.is_bare_leaf:
            return f"BareLeaf({self.path!r})"
        else:
            return f"Leaf({self.display!r} -> {self.path!r})"


# ---------------------------------------------------------------------------
# 解析 mkdocs.yml 的 nav 区域（纯文本解析，不依赖 pyyaml）
# ---------------------------------------------------------------------------
def _find_nav_boundaries(lines: list[str]) -> tuple[int, int]:
    """
    在 mkdocs.yml 文本行中定位 nav 区域的起止行号。
    返回 (nav_start, nav_end)，nav_start 是 "nav:" 所在行，
    nav_end 是 nav 内容最后一行（不含下一个顶级 key）。
    """
    nav_start = None
    for i, line in enumerate(lines):
        if line.rstrip() == "nav:" or re.match(r'^nav:\s', line):
            # 检查是不是顶级 key（行首无缩进）
            if not line.startswith(" "):
                nav_start = i
                break

    if nav_start is None:
        raise ValueError("在 mkdocs.yml 中找不到 'nav:' 顶级键")

    # 寻找下一个顶级 key（行首无缩进，非空行，非注释）
    # nav 内容从 nav_start+1 开始，到下一个顶级 key 前结束
    nav_end = len(lines) - 1
    for i in range(nav_start + 1, len(lines)):
        line = lines[i]
        if line.strip() == "" or line.startswith("#"):
            continue
        if not line.startswith(" ") and not line.startswith("\t"):
            # 这是一个顶级 key
            if re.match(r'^[a-zA-Z_][\w]*\s*:', line):
                nav_end = i - 1
                break

    return nav_start, nav_end


def _get_indent(line: str) -> int:
    """返回一行的前导空格数。"""
    return len(line) - len(line.lstrip(" "))


def parse_nav(mkconfig_path: Path) -> tuple[NavNode, list[str], int, int]:
    """
    从 mkdocs.yml 解析 nav 区域。

    返回:
        root: NavNode 根节点（虚拟根，children 是顶级 nav 条目）
        all_lines: mkdocs.yml 全部行
        nav_start: nav 起始行号
        nav_end: nav 结束行号
    """
    with open(mkconfig_path, "r", encoding="utf-8") as f:
        all_lines = f.readlines()

    nav_start, nav_end = _find_nav_boundaries(all_lines)
    nav_lines = all_lines[nav_start + 1 : nav_end + 1]

    # 确定 nav 内容的基础缩进（第一项相对于 nav: 的缩进）
    base_indent = None
    for line in nav_lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            base_indent = _get_indent(line)
            break

    if base_indent is None:
        base_indent = 2

    root = NavNode(indent=-1)  # 虚拟根

    # 用栈追踪嵌套层级
    # 栈中元素: (node, indent)
    stack: list[tuple[NavNode, int]] = [(root, base_indent - 2)]

    for line in nav_lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        indent = _get_indent(line)

        # 弹出比当前缩进深的节点
        while stack and indent <= stack[-1][1]:
            stack.pop()

        if not stack:
            # 不应该发生，但防御一下
            stack = [(root, base_indent - 2)]

        parent_node = stack[-1][0]
        parent_indent = stack[-1][1]

        # 解析当前行
        # 格式: "- key: value" 或 "- key:" 或 "- value"
        content = stripped
        if content.startswith("- "):
            content = content[2:]  # 去掉 "- "
        elif content == "-":
            # 空占位条目 "-"，跳过
            continue

        # 跳过空内容（如单独的 "-"）
        if not content or not content.strip():
            continue

        # 检查是否是 "key: value" 格式
        colon_idx = content.find(": ")
        if colon_idx >= 0:
            key = content[:colon_idx].strip()
            value = content[colon_idx + 2:].strip()
            if value:
                # 有值 → 命名叶子节点: - 封面: index.md
                node = NavNode(display=key, path=value, indent=indent)
            else:
                # 空值 → 章节头: - 人工智能:
                node = NavNode(display=key, path=None, indent=indent)
        elif content.endswith(":"):
            # 章节头（无空格）: - 主页:
            key = content[:-1].strip()
            node = NavNode(display=key, path=None, indent=indent)
        else:
            # 裸路径或简单值: - MATH/index.md
            # content 本身即是文件路径
            node = NavNode(display=None, path=content, indent=indent)

        node.parent = parent_node
        parent_node.children.append(node)

        # 如果是章节，压入栈以便处理子节点
        if node.is_section:
            stack.append((node, indent))

    return root, all_lines, nav_start, nav_end


# ---------------------------------------------------------------------------
# 生成 nav YAML 文本
# ---------------------------------------------------------------------------
def nav_to_lines(root: NavNode, base_indent: int = 2) -> list[str]:
    """将 NavNode 树转换回 YAML 文本行列表（不含 "nav:" 行）。"""
    lines = []

    def _render(node: NavNode, indent: int):
        prefix = " " * indent + "- "
        if node.is_section:
            # 章节头
            lines.append(f"{prefix}{node.display}:\n")
            for child in node.children:
                _render(child, indent + 2)
        elif node.is_named_leaf:
            # 命名叶子: - key: value
            lines.append(f"{prefix}{node.display}: {node.path}\n")
        elif node.is_bare_leaf:
            # 裸路径: - path
            lines.append(f"{prefix}{node.path}\n")
        # 其他情况（空节点）不输出

    for child in root.children:
        _render(child, base_indent)

    return lines


def write_mkconfig(root: NavNode, all_lines: list[str],
                   nav_start: int, nav_end: int,
                   mkconfig_path: Path, backup: bool = True):
    """将更新后的 nav 树写回 mkdocs.yml。"""
    if backup:
        backup_path = mkconfig_path.with_suffix(mkconfig_path.suffix + ".bak")
        shutil.copy2(mkconfig_path, backup_path)

    new_nav_lines = nav_to_lines(root)

    # 确保 nav: 行后有一个空行（如果原来有的话）
    nav_line = all_lines[nav_start].rstrip()
    if not nav_line.endswith("\n"):
        nav_line += "\n"

    # 重建文件内容
    new_content = (
        all_lines[:nav_start + 1] +   # 包含 nav: 行
        new_nav_lines +
        all_lines[nav_end + 1:]       # nav 之后的内容
    )

    with open(mkconfig_path, "w", encoding="utf-8") as f:
        f.writelines(new_content)


# ---------------------------------------------------------------------------
# 构建目录索引：目录路径 → NavNode（该目录对应的 nav 节点）
# ---------------------------------------------------------------------------
def build_dir_index(node: NavNode, index: dict[str, NavNode] | None = None,
                    prefix: str = "") -> dict[str, NavNode]:
    """
    为 nav 树中每个有意义的目录级别建立索引。

    对于每个叶子节点（文件路径），取其所在目录，
    将该目录映射到它所属的 nav 父节点。

    同时，对于每个章节节点，收集其下所有叶子路径的共同前缀，
    将其映射到该章节节点（用于为新目录找到正确的插入位置）。
    """
    if index is None:
        index = {}

    def _collect_paths(n: NavNode) -> list[str]:
        """收集节点下所有叶子文件的路径。"""
        paths = []
        if n.path is not None:
            paths.append(n.path)
        for child in n.children:
            paths.extend(_collect_paths(child))
        return paths

    for child in node.children:
        # 对于叶子节点，将其父目录映射到父 nav 节点
        if child.path is not None:
            dir_path = os.path.dirname(child.path) + "/" if "/" in child.path else ""
            if dir_path and dir_path != "/":
                dir_path_norm = dir_path.rstrip("/")
                # 记录该目录对应的直接父 nav 节点
                key = f"DIR:{dir_path_norm}"
                if key not in index:
                    index[key] = child.parent

        # 对于章节节点，计算其下所有路径的共同前缀
        if child.is_section:
            all_paths = _collect_paths(child)
            if all_paths:
                # 寻找共同前缀目录
                dirs = [os.path.dirname(p) for p in all_paths if "/" in p]
                if not dirs:
                    dirs = [os.path.dirname(p) for p in all_paths]
                if dirs:
                    common = os.path.commonpath(dirs)
                    if common:
                        key = f"SEC:{common}"
                        if key not in index:
                            index[key] = child

        # 递归处理子节点
        build_dir_index(child, index, prefix)

    return index


def _find_insert_parent(root: NavNode, dir_index: dict[str, NavNode],
                        rel_dir: str) -> NavNode:
    """
    给定一个 docs/ 下的相对目录路径，
    在 nav 树中找到最合适的插入父节点。

    从最具体的目录开始向上查找，返回应插入到的 NavNode。
    """
    # 规范化目录路径
    d = rel_dir.rstrip("/")

    # 1. 首先精确匹配
    key = f"DIR:{d}"
    if key in dir_index:
        return dir_index[key]

    # 2. 章节层级匹配
    key = f"SEC:{d}"
    if key in dir_index:
        return dir_index[key]

    # 3. 逐级向上查找
    parts = d.split("/")
    for i in range(len(parts) - 1, 0, -1):
        parent_dir = "/".join(parts[:i])
        for prefix in ("DIR:", "SEC:"):
            key = f"{prefix}{parent_dir}"
            if key in dir_index:
                return dir_index[key]

    # 4. 返回根节点作为兜底
    return root


# ---------------------------------------------------------------------------
# 同步逻辑
# ---------------------------------------------------------------------------
def _derive_display_name(file_or_dir_name: str) -> str:
    """
    从文件名/目录名推导显示名称。
    - 去掉 .md 后缀
    - 去掉前导数字编号（如 01-, 1.1, Chap1 等）
    """
    name = file_or_dir_name
    if name.endswith(".md"):
        name = name[:-3]
    # 去掉前导数字编号: "01-data-types" → "data-types"
    # name = re.sub(r'^\d+[\.\-\s]*', '', name)
    return name


def add_path_to_nav(root: NavNode, dir_index: dict[str, NavNode],
                    rel_path: str, is_dir: bool = False) -> bool:
    """
    将一个新文件或目录添加到 nav 树中。

    rel_path: 相对于 docs/ 的路径
    is_dir: 是否是目录（目录会在其下文件被添加时自动创建章节节点）

    返回 True 表示有变更。
    """
    if is_dir:
        # 目录本身不需要立即添加；等它的文件被添加时再处理
        return False

    # 检查是否已经在 nav 中
    if _path_exists_in_nav(root, rel_path):
        return False

    # 找到插入位置
    rel_dir = os.path.dirname(rel_path)
    parent_node = _find_insert_parent(root, dir_index, rel_dir)

    # 对于深层目录（相对于最近已知的 nav 节点），可能需要创建中间章节
    # 比如父节点是 "编程语言"，但新文件在 CS/pl/Rust/intro.md
    # 需要创建 "Rust" 章节节点
    known_dir = _get_known_dir_for_node(parent_node, dir_index)

    # 需要创建中间章节的条件：
    # 1. known_dir 非空且不等于 rel_dir（已知目录下还有子目录）
    # 2. known_dir 为空但 rel_dir 非空且 parent_node 是根节点（全新的顶级目录）
    need_intermediate = (
        (known_dir and known_dir != rel_dir) or
        (not known_dir and rel_dir and parent_node is root)
    )

    if need_intermediate:
        # 路径有未知的中间目录 → 需要创建中间章节
        remaining = rel_dir[len(known_dir):].strip("/") if known_dir else rel_dir
        if remaining:
            parts = remaining.split("/")
            current_parent = parent_node
            for part in parts:
                # 检查是否已存在该章节
                existing = _find_child_section(current_parent, part)
                if existing:
                    current_parent = existing
                else:
                    new_section = NavNode(
                        display=_derive_display_name(part),
                        path=None,
                        indent=current_parent.indent + 2
                    )
                    new_section.parent = current_parent
                    # 按字母序插入
                    _insert_sorted(current_parent.children, new_section,
                                   key=lambda n: n.display or n.path or "")
                    current_parent = new_section
            parent_node = current_parent

    # 创建叶子节点
    file_name = os.path.basename(rel_path)
    display = _derive_display_name(file_name)
    leaf = NavNode(display=display, path=rel_path,
                   indent=parent_node.indent + 2)
    leaf.parent = parent_node

    # 检查是否已存在相同路径的节点
    for child in parent_node.children:
        if child.path == rel_path:
            return False

    # 按字母序插入（index.md 排最前）
    _insert_sorted(parent_node.children, leaf,
                   key=lambda n: _sort_key(n))

    # 同时处理 "index.md" 特殊逻辑：如果有 index.md，将其提升为章节的直接路径引用
    # （即把 - index: xxx/index.md 变成 - xxx/index.md，放在章节开头）
    # 实际上这在当前格式中已经通过 display name 处理了

    return True


def _path_exists_in_nav(node: NavNode, rel_path: str) -> bool:
    """检查路径是否已在 nav 树中。"""
    if node.path == rel_path:
        return True
    for child in node.children:
        if _path_exists_in_nav(child, rel_path):
            return True
    return False


def _get_known_dir_for_node(node: NavNode,
                            dir_index: dict[str, NavNode]) -> str:
    """获取 nav 节点对应的已知目录路径。"""
    for key, n in dir_index.items():
        if n is node:
            prefix, path = key.split(":", 1)
            return path
    return ""


def _find_child_section(parent: NavNode, name: str) -> Optional[NavNode]:
    """在父节点的子节点中按名称查找章节。"""
    for child in parent.children:
        if child.is_section and child.display == name:
            return child
    return None


def _sort_key(n: NavNode) -> str:
    """节点的排序键：index.md 排最前，其余按字母序。"""
    name = n.display or n.path or ""
    if name == "index.md" or name.endswith("/index.md") or name == "index":
        return "  !!!000"  # 很靠前的排序
    if name == "index":
        return "  !!!001"
    return name.lower()


def _insert_sorted(children: list[NavNode], new_node: NavNode,
                   key=None):
    """按排序键将新节点插入到有序列表中。"""
    if key is None:
        key = _sort_key
    k = key(new_node)
    for i, child in enumerate(children):
        if key(child) > k:
            children.insert(i, new_node)
            return
    children.append(new_node)


def remove_path_from_nav(root: NavNode, rel_path: str,
                         is_dir: bool = False) -> bool:
    """
    从 nav 树中移除文件或目录的引用。

    返回 True 表示有变更。
    """
    if is_dir:
        return _remove_dir_from_nav(root, rel_path)
    else:
        return _remove_file_from_nav(root, rel_path)


def _remove_file_from_nav(root: NavNode, rel_path: str) -> bool:
    """移除单个文件引用。"""
    for i, child in enumerate(root.children):
        if child.path == rel_path:
            root.children.pop(i)
            return True
        if _remove_file_from_nav(child, rel_path):
            # 如果父节点变成空章节，也清理掉
            _cleanup_empty_sections(root)
            return True
    return False


def _remove_dir_from_nav(root: NavNode, rel_dir: str) -> bool:
    """移除目录下所有文件引用。"""
    changed = False
    rel_dir_prefix = rel_dir.rstrip("/") + "/"

    to_remove = []
    for i, child in enumerate(root.children):
        if child.path and child.path.startswith(rel_dir_prefix):
            to_remove.append(i)
        elif child.is_section:
            # 检查该章节是否完全属于该目录
            if _section_belongs_to_dir(child, rel_dir):
                to_remove.append(i)
            else:
                if _remove_dir_from_nav(child, rel_dir):
                    changed = True

    for i in reversed(to_remove):
        root.children.pop(i)
        changed = True

    _cleanup_empty_sections(root)
    return changed


def _section_belongs_to_dir(node: NavNode, rel_dir: str) -> bool:
    """检查章节节点下的所有文件是否都属于指定目录。"""
    rel_dir_prefix = rel_dir.rstrip("/") + "/"

    def _check(n: NavNode) -> bool:
        if n.path:
            return n.path.startswith(rel_dir_prefix)
        if n.is_section and n.children:
            return all(_check(c) for c in n.children)
        # 空章节
        return True

    if not node.children:
        return True
    return all(_check(c) for c in node.children)


def _cleanup_empty_sections(node: NavNode):
    """递归清理没有子节点的空章节。"""
    to_remove = []
    for i, child in enumerate(node.children):
        if child.is_section:
            _cleanup_empty_sections(child)
            if not child.children:
                to_remove.append(i)
    for i in reversed(to_remove):
        node.children.pop(i)


# ---------------------------------------------------------------------------
# 扫描 docs/ 并同步
# ---------------------------------------------------------------------------
def scan_docs(docs_dir: Path) -> set[str]:
    """
    扫描 docs/ 目录，返回所有 .md 文件的路径集合（相对路径）。
    跳过 SKIP_DIRS 中的目录和 SKIP_FILES 中的文件。
    """
    md_files = set()
    for root, dirs, files in os.walk(docs_dir):
        # 过滤掉要跳过的目录
        dirs[:] = [d for d in dirs
                   if d not in SKIP_DIRS
                   and not d.startswith(".")
                   and not d.startswith("_")]

        for f in files:
            if f in SKIP_FILES:
                continue
            if f.startswith("."):
                continue
            if not f.endswith(".md"):
                continue
            abs_path = os.path.join(root, f)
            rel_path = os.path.relpath(abs_path, docs_dir)
            md_files.add(rel_path)

    return md_files


def scan_docs_dirs(docs_dir: Path) -> set[str]:
    """
    扫描 docs/ 目录，返回所有子目录路径集合（相对路径）。
    """
    dirs_set = set()
    for root, dirs, _files in os.walk(docs_dir):
        dirs[:] = [d for d in dirs
                   if d not in SKIP_DIRS
                   and not d.startswith(".")
                   and not d.startswith("_")]
        for d in dirs:
            abs_path = os.path.join(root, d)
            rel_path = os.path.relpath(abs_path, docs_dir)
            dirs_set.add(rel_path)
    return dirs_set


def collect_nav_paths(node: NavNode) -> set[str]:
    """收集 nav 树中所有文件引用路径。"""
    paths = set()
    if node.path and node.path not in PLACEHOLDER_FILES:
        paths.add(node.path)
    for child in node.children:
        paths.update(collect_nav_paths(child))
    return paths


def sync_docs_to_nav(root: NavNode, docs_dir: Path,
                     dir_index: dict[str, NavNode]) -> list[str]:
    """
    扫描 docs/ 目录并将变化同步到 nav 树。

    返回变更描述列表。
    """
    changes = []

    # 扫描实际文件
    actual_files = scan_docs(docs_dir)

    # nav 中引用的文件
    nav_files = collect_nav_paths(root)

    # 新增的文件
    new_files = actual_files - nav_files
    for rel_path in sorted(new_files):
        if add_path_to_nav(root, dir_index, rel_path):
            changes.append(f"+ 添加: {rel_path}")

    # 删除的文件（不包括占位文件）
    deleted_files = nav_files - actual_files
    for rel_path in sorted(deleted_files):
        if remove_path_from_nav(root, rel_path):
            changes.append(f"- 删除: {rel_path}")

    return changes


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="自动同步 mkdocs.yml nav 与 docs/ 目录",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python3 auto_nav.py              一次性扫描并同步
  python3 auto_nav.py --watch      持续监控 docs/ 变化
  python3 auto_nav.py --watch -i 5 每5秒检查一次
  python3 auto_nav.py --dry-run    只显示变更，不写文件
  python3 auto_nav.py --no-backup  不生成备份文件
        """
    )
    parser.add_argument("--watch", "-w", action="store_true",
                        help="持续监控模式")
    parser.add_argument("-i", "--interval", type=int, default=3,
                        help="监控模式下的轮询间隔（秒），默认 3")
    parser.add_argument("--dry-run", "-n", action="store_true",
                        help="只打印变更，不实际修改 mkdocs.yml")
    parser.add_argument("--no-backup", action="store_true",
                        help="不备份原 mkdocs.yml")
    parser.add_argument("--docs", type=str, default=str(DOCS_DIR),
                        help=f"docs 目录路径（默认: {DOCS_DIR}）")
    parser.add_argument("--config", type=str, default=str(MKCONFIG),
                        help=f"mkdocs.yml 路径（默认: {MKCONFIG}）")

    args = parser.parse_args()

    docs_dir = Path(args.docs)
    config_path = Path(args.config)

    if not docs_dir.is_dir():
        print(f"错误: docs 目录不存在: {docs_dir}", file=sys.stderr)
        sys.exit(1)
    if not config_path.is_file():
        print(f"错误: mkdocs.yml 不存在: {config_path}", file=sys.stderr)
        sys.exit(1)

    if args.watch:
        _run_watch(docs_dir, config_path, args.interval, args.dry_run)
    else:
        _run_sync(docs_dir, config_path, args.dry_run, not args.no_backup)


def _run_sync(docs_dir: Path, config_path: Path,
              dry_run: bool, backup: bool):
    """一次性同步模式。"""
    print("📁 扫描 docs/ 目录...")
    root, all_lines, nav_start, nav_end = parse_nav(config_path)
    dir_index = build_dir_index(root)

    changes = sync_docs_to_nav(root, docs_dir, dir_index)

    if changes:
        print(f"发现 {len(changes)} 处变更:")
        for c in changes:
            print(f"  {c}")

        if not dry_run:
            write_mkconfig(root, all_lines, nav_start, nav_end,
                          config_path, backup=backup)
            print(f"✅ 已更新 {config_path}")
            if backup:
                print(f"   备份保存在 {config_path}.bak")
        else:
            print("[dry-run] 未写入文件")
    else:
        print("✅ nav 已是最新，无需更新")


def _run_watch(docs_dir: Path, config_path: Path,
               interval: int, dry_run: bool):
    """轮询监控模式。"""
    print(f"👀 开始监控 docs/ 目录（每 {interval} 秒检查一次）...")
    print(f"   按 Ctrl+C 停止\n")

    last_md_files = scan_docs(docs_dir)

    try:
        while True:
            time.sleep(interval)

            current_md_files = scan_docs(docs_dir)
            current_dirs = scan_docs_dirs(docs_dir)

            if current_md_files == last_md_files:
                continue

            # 检测变化
            added = current_md_files - last_md_files
            removed = last_md_files - current_md_files

            if not added and not removed:
                continue

            # 重新解析 nav（可能有手动修改）
            root, all_lines, nav_start, nav_end = parse_nav(config_path)
            dir_index = build_dir_index(root)

            changes = sync_docs_to_nav(root, docs_dir, dir_index)

            if changes:
                timestamp = time.strftime("%H:%M:%S")
                print(f"[{timestamp}] 检测到变化:")
                for c in changes:
                    print(f"  {c}")

                if not dry_run:
                    write_mkconfig(root, all_lines, nav_start, nav_end,
                                  config_path)
                    print(f"  → 已更新 mkdocs.yml")
                else:
                    print(f"  → [dry-run] 未写入文件")

            last_md_files = current_md_files

    except KeyboardInterrupt:
        print("\n👋 监控已停止")


if __name__ == "__main__":
    main()
