from time import sleep
from appium import webdriver


class TestBrowser():
    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'browserName': 'Browser',
            'noReset': True,
            'deviceName': '127.0.0.1:7555',
            # 'chromedriverExecutable':'D:\Firefox Download\chromedriver_win32'
            # "appPackage": "com.xueqiu.android",
            # "appActivity": ".view.WelcomeActivityAlias"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("https://m.baidu.com/")
        sleep(5)
