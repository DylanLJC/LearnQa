from time import sleep

from selenium import webdriver


class TestCookiesDemo:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_Cookies(self):
        # 登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        # 获取coockies
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851227064419'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'L18bt7HKL5R_9536Ebbxs-SUpzSqoBQqazmLUVshSDaqc7HkMgCNEDdUSw7JOTCtkrPF5VCdgNH8_1uW5VTaAs_XR37urQdk6_hKlwGmAeNTXQoVZeQ-zTEKAfHjVpXAEAfZmgDprpMKGLAm98wG27DtjJLlOz5v-CW7O7XCunIy9zWkwwqM1at4fnb1BdvM8_wYZm1iYm5PBNAUE0BrDP8f84mETgem6RuZaPOrbYugwUmsg8sFdsKSfiXITQ31Jd8rOI-EMv4qxregDrsVVA'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851227064419'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325075472020'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': '0I_ZNbKacViJTtVnHGWJLuqQJhQSm7WxXQ98Hhygv5HByW_rLVa3LBoc1ReBYAGt'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a4328814'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1654512851, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1622976852'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1622976852'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '10604241933246533'},
            {'domain': '.qq.com', 'expiry': 1623063263, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.15490077.1622976651'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1623008183, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '3pso2uh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False,
             'value': ''},
            {'domain': '.qq.com', 'expiry': 1622976913, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 1686048863, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.40812438.1622976651'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1654512647, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1625568866, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'}]

        for cookie in cookies:  ##为什么用循环语句？   因为是一个列表， add_coockies只能用字典格式，之能一个个遍历遍历到数据中
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        a = self.driver.find_element_by_id('logout').text
        print(a)
        sleep(2)
        # 如有退出按钮则说明断言成功
        assert a == '退出'
