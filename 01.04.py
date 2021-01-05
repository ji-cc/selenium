from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys  #需要引入keys包

# 键盘事件
driver = webdriver.Firefox()   #打开浏览器
driver.get("https://www.zentao.net/user-login.html") # 禅道登录界面

driver.find_element_by_name("account").send_keys("admin")
# 用Tab键把光标移动到密码输入框
driver.find_element_by_name("account").send_keys(Keys.TAB)
time.sleep(8)
driver.find_element_by_name("password").send_keys("123456")
# 使用Enter键按钮
driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(8)


time.sleep(4)
driver.quit()   # 关闭浏览器