# coding=utf-8
from selenium import webdriver
import os
import time

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('drop_down.html')
driver.get(file_path)
time.sleep(2)
# 1. xpath 定位
driver.find_element_by_xpath("/html/body/select/option[4]").click()
time.sleep(3)
# 2. 用option定位
lists = driver.find_elements_by_tag_name("option")  # 用option 定位的是一组元素
# for list in lists:
#     if list.get_attribute("value") == '7.45':
#         list.click()
lists[5].click()    # 数组下标定位
time.sleep(3)
driver.quit()