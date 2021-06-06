from selenium import webdriver
from selenium.webdriver import TouchActions
from time import sleep


class TestTouchAction():
    def setup(self):
        # 不是w3标模式解决
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)

        self.driver = webdriver.Chrome(options=option)  # 将对象添加到浏览器driver里
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        self.driver.get("http://www.baidu.com")
        el = self.driver.find_element_by_id("kw")
        el_search = self.driver.find_element_by_id("su")

        el.send_keys("word")
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()  # 执行该函数

        action.scroll_from_element(el, 0, 10000).perform()
        # sleep(3)
