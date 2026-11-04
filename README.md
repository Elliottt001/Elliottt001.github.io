# 个人笔记

使用 MkDocs Material 构建，正文在 `docs/`，站点资源在 `assets/`，主题覆盖在 `overrides/`。

## 本地预览

建议使用 Python 3.13，与 CI 一致。

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs serve
```

构建和预览不需要 Node.js 或浏览器测试依赖。

## 检查

```sh
mkdocs build
```

CI 只要求构建成功，并生成非空首页和站点样式文件。配置、插件或模板导致的构建错误会阻断发布；笔记的空链接、缺失图片、公式、代码示例和其他内容问题不作为发布门槛。

MkDocs 的警告保留在构建日志中供参考，不启用严格模式，也不设置警告白名单。测试脚本及测试专用依赖文件保留本地，不纳入 Git；本地手动检查也只关注生成页面的基本结构和站点样式，不审核笔记内容。

## 内容与资源

- 页面统计由 `hooks/page_statistics.py` 在 Markdown 渲染后计算，模板在 `overrides/partials/statistics.html`。不要向原始 Markdown 自动插入统计 HTML。
- 列表中的块公式用 `$$`，前后留空行，内容与分隔符保持一致缩进。一级列表里的块公式缩进四个空格。
- 正文链接使用 Markdown 文件路径和明确的 `{#anchor}`；Obsidian 双链需要迁移。教程中演示语法的代码不应批量替换。
- 微积分的补充 SVG 在 `docs/MATH/calculus/res/images/supplements/`，根据所在章节绘制并标为补充图。它们替代遗失截图，不冒充原图。
- 嵌入资源使用 HTTPS；词典示例音频保存在 `docs/CS/tools/res/audio/`，避免再次依赖失效的版本查询地址。
- `docs/assets/`、`site/`、`node_modules/` 是生成目录，不提交。

## 发布

PR 和 main push 都先运行检查。只有 main push 在检查成功后发布已经验证过的站点产物到 `gh-pages`；PR 和手动检查不会部署。
