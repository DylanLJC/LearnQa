from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo0:
    def setup_method(self, method):
        # 功能：在已经打开的浏览器中复用
        option = Options()  ###1复用9222端口，寻找到对应的浏览器的Options
        option.debugger_address = '127.0.0.1:9222'  ###2设置一个默认的debug的环境
        self.driver = webdriver.Chrome(options=option)  ###3设置浏览器的一个参数
        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)  # 增加隐式等待
        self.driver.maximize_window()

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo0(self):
        # self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.LINK_TEXT, "所有分类").click()
        categoryele = self.driver.find_element(By.LINK_TEXT, "所有分类")
        sleep(2)
        assert 'active' == categoryele.get_attribute("class")  # 执行的最后一定要加断言
