from appium import webdriver

from test_app.page.app import App


class TestConteact:
    def setup(self):
        # 创建json串
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        # 完成客户端与服务端的链接
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

        # driver的初始化，app启动
        self.app = App()
        # self.app.start() #方法一，调用接口
        self.main = self.app.start()  # 方法二，通过

    def teardown(self):
        self.app.stop()

    def test_addcontact(self):
        # self.app.goto_main() #方法一，调用接口
        result = self.main.goto_main().goto_addresslist(). \
            goto_addmember().click_addmember_menual(). \
            edit_member().get_tip()
        assert result
