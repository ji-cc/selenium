# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('level_locate.html')
driver.get(file_path)
# 定位link1
# 点击Link1链接（弹出下拉列表）
driver.find_element_by_link_text('Link1').click()
# 定位需要鼠标移动的目标元素
btn = driver.find_element_by_link_text("Action")   # 定位元素
ActionChains(driver).move_to_element(btn).perform()   # 将鼠标移动到目标元素上

time.sleep(6)
driver.quit()
