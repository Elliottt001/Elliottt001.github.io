# 前端内容速查

## 英文词汇

| 缩写 | 英文 | 中文 |
| ---- | ---- | ---- |
|attr|attribute|属性|

## HTML标签

| 标签         | 英文全称                     | 中文说明                           |
|--------------|-----------------------------|----------------------------------|
| `a`          | Anchor                      | 链接 / 锚点                         |
| `abbr`       | Abbreviation                | 缩写词                            |
| `address`    | Address                     | 地址                              |
| `b`          | Bold                        | 粗体（文本）                       |
| `bdo`        | Bi-Directional Override     | 文本显示方向                       |
| `blockquote` | Block Quotation             | 区块引用语                         |
| `br`         | Break                       | 换行                              |
| `cite`       | Citation                    | 引用                              |
| `code`       | Code                        | 源代码（文本）                     |
| `dd`         | Definition Description      | 定义列表中对术语的说明              |
| `del`        | Deleted                     | 删除（的文本）                     |
| `dfn`        | Defines a Definition Term   | 正在定义的术语（行内元素）          |
| `div`        | Division                    | 分隔                              |
| `dl`         | Definition List             | 定义列表                           |
| `dt`         | Definition Term             | 定义列表中的术语                    |
| `em`         | Emphasized                  | 加重（文本）                       |
| `h1`~`h6`      | Header 1 to Header 6        | 标题1到标题6                       |
| `hr`         | Horizontal Rule             | 水平尺                            |
| `i`          | Italic                      | 斜体（文本）                       |
| `iframe`     | Inline frame                | 嵌入页面                       |
| `ins`        | Inserted                    | 插入（的文本）                     |
| `kbd`        | Keyboard                    | 键盘（文本）                       |
| `li`         | List Item                   | 列表项目                           |
| `ol`         | Ordered List                | 排序列表                           |
| `optgroup`   | Option group                | 定义选项组                         |
| `p`          | Paragraph                   | 段落                              |
| `pre`        | Preformatted                | 预定义格式（文本）                 |
| `q`          | Quotation                   | 引用语                            |
| `s`   | Strikethrough               | 删除线                            |
| `samp`       | Sample                      | 示例（文本）                       |
| `small`      | Small                       | 变小（文本）                       |
| `span`       | Span                        | 范围                              |
| `strong`     | Strong                      | 加重（文本）                       |
| `sub`        | Subscripted                 | 下标（文本）                       |
| `sup`        | Superscripted               | 上标（文本）                       |
| `td`         | table data cell             | 表格中的一个单元格                 |
| `th`         | table header cell           | 表格中的表头                       |
| `tr`         | table row                   | 表格中的一行                       |
| `u`          | Underlined                  | 下划线（文本）                     |
| `ul`         | Unordered List              | 不排序列表                         |
| `var`        | Variable                    | 变量（文本）                       |

`cell` / `nl` 不是标准 HTML 标签。表格单元格是 `td` / `th`，导航区是 `nav`，列表仍用 `ul` / `ol` / `li`。

## 属性：写在开始标签里面

```html
<a href="https://example.com">链接</a>
<img src="photo.png" alt="照片说明">
```

`a` / `img` 是元素，`href` / `src` / `alt` 是属性，不要当成标签背。

| 属性 | 用途 |
| --- | --- |
| `href` | 链接目标 |
| `src` | 图片、脚本等资源地址 |
| `alt` | 图片的替代文字，图片加载失败或读屏时有用 |
| `rel` | 当前文档与链接资源的关系，如 stylesheet |
| `cellpadding` / `cellspacing` | 旧表格属性，现在用 CSS 的 padding / border-spacing |

## 旧标签

下面这些会在旧教程里见到，新页面尽量不用：

| 旧标签 | 现在的写法 |
| --- | --- |
| `acronym` | `abbr` |
| `big` / `font` | CSS 控制字号、字体、颜色 |
| `center` | CSS 控制对齐 |
| `tt` | 代码用 `code`，等宽字体用 CSS |
| `strike` | 删除内容用 `del`，不再适用的内容用 `s` |
