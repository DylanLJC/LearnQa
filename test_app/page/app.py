# 存放app的相关操作，打开重启，关闭
from test_app.page.main_page import MainPage


# 存放app的操作：启动app重新启动、关闭、进入主页main

class App:
    def start(self):
        return self  # 方法二：切换页面用return，不切换直接返回本页面

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        # 入口
        return MainPage()
