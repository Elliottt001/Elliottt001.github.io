`ctrl + N` 建立文档

双链：`[[]]`

- 反向链接：提到了这篇的笔记
- 出链：这篇中包含的其他笔记
- 在右侧的出链、包含的链接处查看，也包含潜在链接，可以一键转为链接

标签：`#内容`：

- 点击这个标签即可在搜索框中查看所有该标签
- 右上角标签图标

白板

- 底下图标添加笔记
- 添加内容
- 分组
- 关系
- 调色


### 快捷键

`ctrl + p` 命令面板


### 插件

关闭安全模式

科学上网

#### 看板

左侧工具栏

#### readitlater
左侧工具栏

#### tasks

选中任务（- [ ] ），输入 `ctrl + p` ，输入 create or edit task 


#### setting search

搜索设置

#### easy typing

文本自动加工


#### templater
是一种编程语言
通过命令，实现功能

[templater官方网站](https://silentvoid13.github.io/Templater/)

例子：

- 创建时间：`<% tp.file.creation_date()%>`
- 指定文件路径：`<% await tp.file.move("/path/" + tp.file.title) %>`

使用：打开第三方插件templater，指定模板文件位置

#### dataview

```dataview
TABLE aliases as "昵称",dateformat(birthday,"MMM dd") as "生日",type as "分组"
from "🌊 001 RIVER · 河流/012 People 联系人"
WHERE birthday != null
sort birthday.month, birthday.day asc
```

### 模板

新建文件夹（放模板）—— 建立并写入文件 —— 核心插件/日记/模板位置

### 日记

- 点击右上角日历图标，点日期，建立or打开对应日期的日记文档

### 文档属性

文档属性是位于文档开头的 YAML 块，用 `---` 包裹。它可以包含键值对，用于定义文档的元数据，例如用于存储标题、标签、日期、作者等信息例如：
```yaml
---
title: 我的文档
tags: [笔记, 教程]
date: 2023-10-01
author: 张三
---
```


**常用的文档属性字段**
以下是一些常见的文档属性字段：
- **`title`**: 文档标题。
- **`tags`**: 文档标签，可以是单个标签或多个标签的列表。
- **`date`**: 文档创建或修改日期。
- **`alias`**: 文档别名，用于链接时使用。
- **`author`**: 文档作者。
- **`category`**: 文档分类。
- **`description`**: 文档描述。


**模板中使用属性**
- 如果你使用 **Templater** 插件，可以在模板中动态插入文档属性。例如：
  ```markdown
  ---
  title: <% tp.file.title %>
  date: <% tp.date.now("YYYY-MM-DD") %>
  ---
  ```

#### 别名
别名可以代替原名

