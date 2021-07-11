# 存放app的相关操作，打开重启，关闭
from appium import webdriver

from test_app.page.main_page import MainPage


# 存放app的操作：启动app重新启动、关闭、进入主页main

class App:
    def start(self):
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

        return self  # 方法二：如果切换页面不返回return，不切换直接返回本页面

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        # 入口
        return MainPage(self.driver)
