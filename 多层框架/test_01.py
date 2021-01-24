# 多层窗口定位

# coding=utf-8
from selenium import webdriver
import time
import os

browser = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('frame.html')
browser.get(file_path)
browser.implicitly_wait(30)
# 从默认页面跳转到id=f2页面
# 先找到到ifrome1（id = f1）
browser.switch_to.frame("f1")
# 再找到其下面的ifrome2(id =f2)
browser.switch_to.frame("f2")

# 下面就可以正常的操作元素了
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)

# 定位 click 元素，跳转到默认页面
browser.switch_to.default_content()
browser.switch_to.frame("f1")
browser.find_element_by_link_text("click").click()
time.sleep(6)

browser.quit()