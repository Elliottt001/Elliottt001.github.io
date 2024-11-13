```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.edge.service import Service

# 初始化 WebDriver
driver = webdriver.Edge()
service = Service()
url = 'https://movie.douban.com/top250'
driver.get(url)

result_list = []

for i in range(0, 2):
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
        
        # 在这里，实际上要进行数据获取的操作
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
# Copyright © 2024 张瑞喆 All rights reserved.
```
