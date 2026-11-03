# MkDocs

[mkdocs official](https://github.com/squidfunk/mkdocs-material/)

[mkdocs.yml official](https://github.com/squidfunk/mkdocs-material/blob/master/mkdocs.yml)

[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

## 提示块

`!!!` 是直接展开，`???` 是可以折叠。标题用双引号，正文往里缩进 4 个空格。

```markdown
!!! info "标题"

    正文放这里。
```

里面可以放标题、列表、代码，但层级要正确。代码注释中的 `#` 不是页面标题，最好在页面开头自己写清楚一级标题。

## 图标和 Emoji

[图标与 Emoji 查询入口](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/)在 Material 文档里。把文档里的搜索框 HTML 复制过来不会自动带上查询逻辑，直接去入口查 shortcode。

:smile:
:fontawesome-regular-face-laugh-wink:
[点击查看公式写法](markdown-advanced.md#16-latex)
:octicons-heart-fill-24:{ .heart }

|2024.11.11 |2024.11.22           |
|-----------|---------------------|
|hello      |world                |
|`#!C int a`|`#! py import random`|

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Set up in 5 minutes__

    ---

    Install [`mkdocs-material`](#) with [`pip`](#) and get up
    and running in minutes

    [:octicons-arrow-right-24: Getting started](#)

-   :fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__

    ---

    Focus on your content and generate a responsive and searchable static site

    [:octicons-arrow-right-24: Reference](#)

-   :material-format-font:{ .lg .middle } __Made to measure__

    ---

    Change the colors, fonts, language, icons, logo and more with a few lines

    [:octicons-arrow-right-24: HTML](#)

-   :material-scale-balance:{ .lg .middle } __Open Source, MIT__

    ---

    Material for MkDocs is licensed under MIT and available on [GitHub]

    [:octicons-arrow-right-24: CSS](#)

</div>

![Image title](https://dummyimage.com/600x400/){ width="300" }
/// caption
Image caption
///