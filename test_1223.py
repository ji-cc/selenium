from selenium import  webdriver
import time
from selenium.webdriver.common.keys import Keys  # 需要引入keys包
from selenium.webdriver.common.action_chains import ActionChains   # 引入键盘事件所需要的包

driver = webdriver.Firefox()   #打开浏览器
driver.get("https://www.baidu.com/")  # 百度网页
# 最大化浏览器
# driver.maximize_window()

# 最小化浏览器
# driver.minimize_window()

# 设置浏览器的宽和高
# driver.set_window_size(400, 800)
# time.sleep(4)

# # id 的定位
# driver.find_element_by_id("kw").send_keys("三十而已")  #  在百度网页右键检查百度搜索框的id是“kw”, 搜索"三十而已"
# driver.find_element_by_id("su").click()   # 点击“百度一下”的按钮，检查到该按钮的id是su

# # name的定位   不是每个元素都有name属性
# driver.find_element_by_name("wd").send_keys("yamy")
# driver.find_element_by_id("su").click()   # “百度一下” 的按钮没有name属性，所有还是用id定位

# class name的定位   # 必须保证class name 的属性只有一个并且唯一，才能用class name定位
# driver.find_element_by_class_name("s_ipt").send_keys("java")
# driver.find_elements_by_class_name("bg s_btn").click()
# driver.find_element_by_id("su").click()

# link text 定位    # 只能定位链接，定位到链接之后点击就行
# driver.find_element_by_link_text(u"视频").click()

# partial link text 部分链接定位
# driver.find_element_by_partial_link_text("hao").click()

# tag name 定位
# driver.find_element_by_tag_name("input").send_keys(u"太白山")   #使用Input标签定位不到百度搜索框，因为使用input标签的很多
# driver.find_element_by_id("su").click()

# xpath 定位
# driver.find_element_by_xpath("//*[@id='kw']").send_keys(u"太白山")
# driver.find_element_by_xpath("//*[@id='su']").click()

# CSS 定位
# driver.find_element_by_css_selector("#kw").send_keys("雪橇三傻")
# driver.find_element_by_xpath("//*[@id='su']").click()

# driver.find_element_by_id("kw").send_keys("三十而已")
# driver.find_element_by_id("su").click()
# time.sleep(2)
# 清除百度搜索框的内容
# driver.find_element_by_id("kw").clear()
# driver.find_element_by_id("kw").send_keys("四十不惑")
# driver.find_element_by_id("su").click()

# submit 提交 == 点击
driver.find_element_by_id("kw").send_keys("乃万")
# driver.find_element_by_id("su").submit()
time.sleep(4)
# 设置等待时间
# 固定等待时间
# time.sleep(10)
# 智能等待时间，页面加载完成后，不需要固定等待10s，可以立即点击
# driver.implicitly_wait(20)
# driver.find_element_by_link_text("乃万(豆瓣)").click()

# 打印信息(只能打印前一个网页的title和URL)
# 打印title url
# title = driver.title
# print("title = "+title)
# url = driver.current_url
# print("URL = "+url)
# time.sleep(6)
# # 浏览器的滚动条拖动到最低端
# js = "var q=document.documentElement.scrollTop=100000"
# driver.execute_script(js)
# time.sleep(6)
# # 浏览器的滚动条推动到最顶端
# js0 = "var q=document.documentElement.scrollTop=0"
# driver.execute_script(js0)

# 组合键盘事件
# 复制 ctrl+a      先定位到要复制的输入框，再发送组合键
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
time.sleep(4)
# 剪贴   ctrl+x
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
time.sleep(4)

driver.find_element_by_id("kw").send_keys("赵丽颖")
# 定位到“百度一下”按钮
su1 = driver.find_element_by_id("su")
# 右击
ActionChains(driver).context_click(su1).perform()
# 双击
time.sleep(5)
ActionChains(driver).double_click(su1).perform()

time.sleep(5)
title = driver.find_element_by_id("su")
target = driver.find_element_by_link_text("赵丽颖-百度百科 ")
# 拖动  从“百度一下”拖动到“百度百科”
ActionChains(driver).drag_and_drop(title, target).perform()

# 移动 把鼠标移动到目标元素上
ActionChains(driver).move_to_element(target).perform()



# text 获取文本内容
# text = driver.find_element_by_id("s-bottom-layer-right").text
# print(text)


time.sleep(4)
driver.quit()   # 关闭浏览器