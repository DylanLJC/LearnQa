from selenium import webdriver


class BasePage:
    """
    提供与页面无关的封装，比如driver初始化
    """
    base_url = ""

    def __init__(self, base_driver=None):

        if base_driver is None:
            # 功能：通过remote复用浏览器
            chrome_arg = webdriver.ChromeOptions()  ###1复用9222端口，寻找到对应的浏览器的Options
            chrome_arg.debugger_address = '127.0.0.1:9222'  ###2设置一个默认的debug的环境
            self.driver = webdriver.Chrome(options=chrome_arg)  ###3设置浏览器的一个参数
            # 打开首页
            # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.driver.get(self.base_url)
            self.driver.implicitly_wait(3)
        else:
            self.driver: webdriver = base_driver  #:webdriver 注解无实际意义

    def find(self, by, locator=None):
        # 只传入一个元组参数
        if locator is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by, value=locator)
