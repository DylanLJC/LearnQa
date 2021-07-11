# 完成基本内容的封装，比如初始化driver、find、find and click
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver  # 建立启动的实例

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def find_and_click(self, by, value):
        self.find(by, value).click()

    def find_and_send(self, by, value, text):
        self.find(by, value).send_keys(text)
