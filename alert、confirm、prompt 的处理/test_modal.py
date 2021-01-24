from selenium import webdriver
import time
import os
driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('alert.html')
driver.get(file_path)
# 点击click