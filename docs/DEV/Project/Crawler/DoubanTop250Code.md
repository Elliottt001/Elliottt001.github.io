```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.chrome.service import Service

# 自动更新 ChromeDriver
# from webdriver_manager.chrome import ChromeDriverManager
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

# 初始化 WebDriver
driver = webdriver.Chrome()
service = Service()
url = 'https://movie.douban.com/top250'
driver.get(url)

result_list = []

for i in range(0, 10):
    element_hds = driver.find_elements(By.CLASS_NAME, 'hd')
    for element_hd in element_hds:
        data_dict = {
            "title": "",
            "short": "",
            "score": "",
        }
        element_a = element_hd.find_element(By.TAG_NAME, 'a')
        herf = element_a.get_attribute('href')
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(herf)
        
        # 数据获取
        title = driver.find_element(By.TAG_NAME, 'h1').text
        data_dict['title'] = title
        short = driver.find_element(By.CLASS_NAME, 'short').text
        data_dict['short'] = short
        score = driver.find_element(By.CLASS_NAME, 'rating_num').text
        data_dict['score'] = score

        result_list.append(data_dict)
        
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    next_element = driver.find_element(By.CLASS_NAME, 'next')
    next_element_a = next_element.find_element(By.TAG_NAME, 'a')
    next_element_a.click()

print(result_list)

df = pd.DataFrame(result_list)

df.to_excel('doubanTop250.xlsx', index=False)

# 关闭浏览器
driver.quit()

# 这时候你可以去吃饭去了，爬这些数据得一段时间了
print('爬取完成,已生成excel文件')

# Copyright © 2024 张瑞喆 All rights reserved.
```
