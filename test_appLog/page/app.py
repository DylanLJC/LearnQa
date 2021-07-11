# 存放app的相关操作，打开重启，关闭
from appium import webdriver

from test_appLog.page.main_page import MainPage

# 存放app的操作：启动app重新启动、关闭、进入主页main
from test_appLog.page.base_page import BasePage


class App(BasePage):
    def start(self):
        if self.driver == None:
            print("driver 为空")
            # 创建jsion串
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
        else:
            # 启动也页面launch_app()
            self.driver.launch_app()

        return self  # 方法二：如果切换页面不返回return，不切换直接返回本页面

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        # 入口
        return MainPage(self.driver)
