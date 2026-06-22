# 网络数据采集

本章整合了「网络数据采集概述」「用 Python 获取网络数据」「用 Python 解析 HTML 页面」三部分内容，覆盖爬虫的概念、HTTP 基础、`requests` 抓取、XPath / CSS 选择器解析等核心知识。

## 1. 爬虫概述

爬虫（crawler）也常被称为网络蜘蛛（spider），是按照一定规则自动浏览网站并获取所需信息的机器人程序，被广泛应用于互联网搜索引擎和数据采集。网页中除了供阅读的文字之外，还包含超链接，爬虫正是通过这些链接不断获得其它页面的地址，持续进行数据采集。

### 爬虫的应用领域

理想状态下，所有 ICP（Internet Content Provider）都为自己的网站提供 API 供其他程序获取共享数据，但这类 API 通常对抓取数据量和频率有限制。对企业而言，及时获取行业数据和竞对数据非常重要，合理利用爬虫便显得至关重要。常见应用领域包括：

1. 搜索引擎
2. 新闻聚合
3. 社交应用
4. 舆情监控
5. 行业数据

### 爬虫合法性

“爬虫写得好，牢饭吃到饱” —— 编程爬虫程序是否违法？可以从以下角度解读：

1. 网络爬虫目前尚处拓荒阶段，Robots 协议（“网络爬虫排除标准”）确立了道德规范，但法律部分仍在完善中，属于灰色地带。
2. “法不禁止即为许可”——若爬虫只是像浏览器一样获取前端展示的公开数据，而非后台私密数据，一般不必担心法律约束。
3. 爬取时应遵守 Robots 协议，控制抓取速度；使用数据时尊重知识产权。
4. 适当隐匿身份，避免被举证爬虫破坏对方动产（如服务器）。
5. 不要在公网（如代码托管平台）开源或展示爬虫代码。

#### Robots 协议

大多数网站会定义 `robots.txt` 文件，这是一个君子协议。以淘宝的 `robots.txt` 为例：

```
User-agent: Baiduspider
Disallow: /

User-agent: baiduspider
Disallow: /
```

淘宝禁止百度爬虫爬取它的任何资源。

### HTTP 基础

HTTP 是浏览器与 Web 服务器之间传输数据的载体。HTTP 请求由请求行、请求头、空行、消息体四部分构成；请求行包含请求方法（GET、POST 等）、资源路径和协议版本。HTTP 响应同样由响应行、响应头、空行、消息体构成，响应行中包含协议版本和状态码。

### 辅助工具

开发爬虫时常用的辅助工具：

1. **Chrome Developer Tools** — Elements / Console / Sources / Network / Application 五个面板，分别用于查看 HTML、执行 JS、调试源代码、查看请求和本地存储。
2. **Postman** — 网页调试与 RESTful 请求工具。
3. **HTTPie** — 命令行 HTTP 客户端。

   ```bash
   pip install httpie
   http --header https://movie.douban.com/
   ```

4. **`builtwith`** — 识别网站所用技术的工具。

   ```python
   import builtwith
   print(builtwith.parse('http://www.bootcss.com/'))
   ```

5. **`python-whois`** — 查询网站所有者。

   ```python
   import whois
   print(whois.whois('https://www.bootcss.com'))
   ```

### 爬虫的基本工作流程

一个基本的爬虫通常由数据采集（下载）、数据处理（解析）、数据存储（持久化）三部分构成。一般步骤：

1. 设定抓取目标并获取网页。
2. 服务器无法访问时，按指定重试次数尝试重新下载。
3. 必要时设置 User-Agent 或隐藏真实 IP。
4. 对返回页面进行解码并抽取所需信息。
5. 用正则表达式等方式从页面中抽取链接。
6. 对链接进一步处理（递归获取）。
7. 将有用信息持久化。

## 2. 用 requests 获取网络数据

`requests` 是 Python 中获取 HTTP/HTTPS 资源最常用的三方库，对标准库进行了封装，简化了网络访问的操作。

### 抓取 HTML

```python
import requests

resp = requests.get('https://www.sohu.com/')
if resp.status_code == 200:
    print(resp.text)
```

> `resp.status_code` 获取响应状态码，`resp.text` 是页面 HTML 字符串。

可以结合正则表达式从字符串中抽取内容：

```python
import re
import requests

pattern = re.compile(r'<a.*?href="(.*?)".*?title="(.*?)".*?>')
resp = requests.get('https://www.sohu.com/')
if resp.status_code == 200:
    for href, title in pattern.findall(resp.text):
        print(href)
        print(title)
```

### 下载二进制资源

```python
import requests

resp = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')
with open('baidu.png', 'wb') as f:
    f.write(resp.content)
```

> `resp.content` 是服务器响应的二进制数据。

### 完整示例：抓取豆瓣 Top250

```python
import random
import re
import time
import requests

for page in range(1, 11):
    resp = requests.get(
        url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
        # 不设置 User-Agent，豆瓣会检测出非浏览器并阻止请求
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
    )
    pattern1 = re.compile(r'<span class="title">([^&]*?)</span>')
    pattern2 = re.compile(r'<span class="rating_num".*?>(.*?)</span>')
    for title, rank in zip(pattern1.findall(resp.text), pattern2.findall(resp.text)):
        print(title, rank)
    time.sleep(random.random() * 4 + 1)
```

> 通过分析 robots 协议，豆瓣并不拒绝百度爬虫，因此也可以将 `User-Agent` 设为 `'BaiduSpider'`。

### 使用 IP 代理

为了避免被基于 IP 的反爬封禁，需要使用商业 IP 代理（蘑菇代理、芝麻代理、快代理等）。蘑菇代理 HTTP 隧道接入示例：

```python
import requests

APP_KEY = 'Wnp******************************XFx'
PROXY_HOST = 'secondtransfer.moguproxy.com:9001'

resp = requests.get(
    url='https://movie.douban.com/top250',
    headers={
        'Proxy-Authorization': f'Basic {APP_KEY}',
        'User-Agent': 'Mozilla/5.0 ...',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4'
    },
    proxies={
        'http': f'http://{PROXY_HOST}',
        'https': f'https://{PROXY_HOST}'
    },
    verify=False
)
```

## 3. 解析 HTML 页面

正则表达式可以解析 HTML，但表达式难写、易错。下面介绍另外两种主流方式：XPath 与 CSS 选择器。

### HTML 页面结构

```html
<!doctype html>
<html>
    <head>
        <!-- 页面元信息：字符编码、标题、关键字、媒体查询等 -->
    </head>
    <body>
        <!-- 页面主体：显示在浏览器窗口中的内容 -->
    </body>
</html>
```

标签、CSS、JavaScript 是构成 HTML 页面的三要素：标签承载内容，CSS 负责渲染，JavaScript 控制交互。

### XPath 解析

XPath 原本是 XML 的查询语法，使用路径表达式选取节点。XML 示例：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
    <book>
      <title lang="eng">Harry Potter</title>
      <price>29.99</price>
    </book>
    <book>
      <title lang='zh'>Learning XML</title>
      <price>39.95</price>
    </book>
</bookstore>
```

常用 XPath 表达式：

| 路径表达式 | 含义 |
| --- | --- |
| `/bookstore` | 选取根元素 bookstore |
| `//book` | 选取所有 book 元素，不论位置 |
| `//@lang` | 选取名为 lang 的所有属性 |
| `/bookstore/book[1]` | 第一个 book 子元素 |
| `/bookstore/book[last()]` | 最后一个 book 元素 |
| `//title[@lang='eng']` | 拥有 lang="eng" 的 title 元素 |
| `/bookstore/book[price>35.00]` | price > 35 的 book 元素 |
| `/bookstore/*` | bookstore 的所有子元素 |
| `//book/title \| //book/price` | book 下的所有 title 和 price |

实现 XPath 解析需要 `lxml`：

```bash
pip install lxml
```

用 XPath 改写豆瓣 Top250 示例：

```python
from lxml import etree
import requests

for page in range(1, 11):
    resp = requests.get(
        url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
        headers={'User-Agent': 'BaiduSpider'}
    )
    tree = etree.HTML(resp.text)
    title_spans = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]')
    rank_spans  = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[2]')
    for t, r in zip(title_spans, rank_spans):
        print(t.text, r.text)
```

> 在 Chrome 开发者工具中右键元素 → Copy → Copy XPath 即可获得元素的 XPath。

### CSS 选择器解析（BeautifulSoup）

对于熟悉 CSS 的开发者，CSS 选择器更直观。Python 中可用 `beautifulsoup4` 或 `pyquery`：

```bash
pip install beautifulsoup4
```

```python
import bs4
import requests

for page in range(1, 11):
    resp = requests.get(
        url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
        headers={'User-Agent': 'BaiduSpider'}
    )
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    title_spans = soup.select('div.info > div.hd > a > span:nth-child(1)')
    rank_spans  = soup.select('div.info > div.bd > div > span.rating_num')
    for t, r in zip(title_spans, rank_spans):
        print(t.text, r.text)
```

### 三种解析方式对比

| 解析方式 | 对应模块 | 速度 | 难度 |
| --- | --- | --- | --- |
| 正则表达式 | `re` | 快 | 困难 |
| XPath | `lxml` | 快 | 一般 |
| CSS 选择器 | `bs4` / `pyquery` | 不确定 | 简单 |
