from selenium import webdriver
import time
import os
driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('upload.html')
driver.get(file_path)
time.sleep(10)
# 定位上传文件按钮
driver.find_element_by_tag_name("input").send_keys("C:/Users/asus-pc/Desktop/1.jpeg");
time.sleep(7)
driver.quit()