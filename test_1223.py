from selenium import  webdriver
import time

driver = webdriver.Firefox()   #打开浏览器
driver.get("https://www.baidu.com/")  # 百度网页
# 最大化浏览器
driver.maximize_window()
time.sleep(4)

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
driver.find_element_by_id("su").submit()
# 设置等待时间
# 固定等待时间
time.sleep(10)

driver.find_element_by_partial_link_text("乃万_百度百科").click()

# text 获取文本内容
# text = driver.find_element_by_id("s-bottom-layer-right").text
# print(text)




time.sleep(4)
driver.quit()   # 关闭浏览器