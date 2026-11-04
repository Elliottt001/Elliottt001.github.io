# 个人笔记

使用 MkDocs Material 构建，正文在 `docs/`，站点资源在 `assets/`，主题覆盖在 `overrides/`。

## 本地预览

建议使用 Python 3.13 和 Node.js 24，与 CI 一致。

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
npm ci
npx playwright install chromium
mkdocs serve
```

只构建或预览网站时，可以仅安装 `requirements.txt`，不需要 Node.js 和浏览器测试依赖。

## 检查

```sh
mkdocs build 2>&1 | tee build.log
python tests/site-content.test.py
python tests/site-theme.test.py
python tests/site-rendering.test.py site build.log
python tests/cs-notes.test.py
npm test
npm run test:browser
```

代码示例检查需要 `clang` 和 `clang++`。浏览器检查使用本地安装的同版本 MathJax，验证实际公式、辅助 MathML、手机宽度、搜索、音频和补充图，不依赖测试时 CDN 是否可访问。

目前导航中保留 `none.md`、`1.md` 两个已有占位路径。构建仍显示这两条警告，渲染检查只允许这两条已知警告，新增警告会让 CI 失败。导航覆盖率另行整理。

## 内容与资源

- 页面统计由 `hooks/page_statistics.py` 在 Markdown 渲染后计算，模板在 `overrides/partials/statistics.html`。不要向原始 Markdown 自动插入统计 HTML。
- 列表中的块公式用 `$$`，前后留空行，内容与分隔符保持一致缩进。一级列表里的块公式缩进四个空格。
- 正文链接使用 Markdown 文件路径和明确的 `{#anchor}`；Obsidian 双链需要迁移。教程中演示语法的代码不应批量替换。
- 微积分的补充 SVG 在 `docs/MATH/calculus/res/images/supplements/`，根据所在章节绘制并标为补充图。它们替代遗失截图，不冒充原图。
- 嵌入资源使用 HTTPS；词典示例音频保存在 `docs/CS/tools/res/audio/`，避免再次依赖失效的版本查询地址。
- `docs/assets/`、`site/`、`node_modules/` 是生成目录，不提交。

## 发布

PR 和 main push 都先运行检查。只有 main push 在检查成功后发布已经验证过的站点产物到 `gh-pages`；PR 和手动检查不会部署。
