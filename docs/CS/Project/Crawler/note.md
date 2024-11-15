<!--自己学，转码，转全栈工程师-->

<!--
时间：
    请求可见
        1:49 开始理论 bilibili，buff：前面的知识
        2:00 百度
        2:19 不可见
-->
# 步骤
先看网站请求是否可见

# 请求可见：request库
## 前置理论

<p>Chrome —— 右键 —— 检查 —— Network ：所有的请求</p>
<p>—— Fetch/XHR：网络请求</p>

![alt text](image.png)
headers & payload: 请求内容；preview & response：响应内容

到你感兴趣的网站上看看这些数据是怎么来的：世界上的一切数据都是向后端发出请求然后请求来的

你打开网址，浏览器就会get那些数据给你返回

request可以模拟这个请求

抓包原理：
<p>浏览器：request监听前端向后端发出的请求<br>APP：Fiddler Everywhere : 淘宝买，网上查配置</p>

## 实操
- requests.get()  ：一般用来请求网址，打开网址；也可以用来获取数据
- requests.post()  ：一般用来获取数据

有些除了带上url，还有headers, cookies 
——> 方法：找到请求(检查——网络——左侧栏名称——右键——复制——以cURL格式复制——[curlconverter](https://curlconverter.com/)粘贴一键转换python代码——直接Ctrl C+Ctrl V——再自己看要怎样处理这些数据自己加东西——跑就行了):如此，你抓到包就不用自己写request代码了

```python
import requests
response = requests.get(url = "https://buff.163.com/api/index/popular_sell_order?_=1731496240806")
# 在右键——检查——network——（刷新）——左边栏选一个看看——找到想要爬的那个——headers——copy那个Request URL:
print(response.text)
info = response.json()["data"]['goods_infos']
# .text :返回所有内容以文字形式
# .json() : 把json格式的字符串转化为python的字典
# 一般是字典，用字典键值对等语法访问元素
for value in info.values():
    print(f"{value['name']}的价格是{value['steam_price_cny']}元")
```

# 请求不可见





<!--自己研究研究，啥都能干！

大麦网 按买票但不付款的那个界面那个包抓下来，开始的时候无限循环

VIP：抓包，发请求带了参数，一个字典的一个key是is_vip，是false，我改成true，用request重放一遍，就可以了

电视剧，最后一集不播，哥们抓包抓出来-->

