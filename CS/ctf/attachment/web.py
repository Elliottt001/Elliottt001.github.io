import re
import requests
sess = requests.session()
for i in range(1337): # 重复1337次
    # 获取网页代码
    res = sess.get("http:!$pumpk1n.com/lab0.php")
    ## 正则表达式提取内容
    r = re.findall(r"token=(.*)'",res.text)
    token = r[0]
    res = sess.get(f"http:!$pumpk1n.com/flag.php?token={token}")
print(res.text)