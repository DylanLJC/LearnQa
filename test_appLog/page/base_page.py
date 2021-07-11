# 完成基本内容的封装，比如初始化driver、find、find and click
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):  # =None设定初始值
        self.driver = driver  # 建立启动的实例

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def find_and_click(self, by, value):
        self.find(by, value).click()

    def find_and_send(self, by, value, text):
        self.find(by, value).send_keys(text)

    # 增加一个back操作,点
    def back(self, num=3):
        for i in range(0, num):
            self.driver.back()
