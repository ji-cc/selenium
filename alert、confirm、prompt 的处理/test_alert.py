# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os
driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('alert.html')
driver.get(file_path)
# 定位点击按钮
driver.find_element_by_id("tooltip").click()
time.sleep(8)
alert = driver.switch_to.alert   # 定位到弹出来的 alert 框
# 输出弹出框的内容
text = alert.text
print("text = "+text)
alert.accept()  # 弹出框消失
time.sleep(8)
driver.quit()   # 关闭浏览器