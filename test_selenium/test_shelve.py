import shelve
from lib2to3.pgen2 import driver
from time import sleep

from selenium import webdriver

##这是我要提交的作业
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
        # cookies = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False,
        #      'value': ''},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': 'tB3vbqx0izk95CrFS9yq8ZE0qRuNveVLHycQ5XhLxW6JQNt7Kahs6c-dhXN2nYUHgGWpi6ajOq2EgO1A3MmXoVNgzty2VyLB-RD7Cg8iziI1ATpRIT2babE4fBYElIW_UDUzwqpNavzTXXmsCeoVPikhtHZa57vLpT2xoOqJeqmAr6k53JGsshehqUwLUDroe_VEZTWQPII5zvVOF_67VodarlHkU7TSaIMMcVv1yoyE58_0KnpwnNhZamm65_3ozVbDisJFOw4LVvqXEKCSLg'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688851227064419'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970325075472020'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': '0I_ZNbKacViJTtVnHGWJLnuW2zbtTm6GbwoUV6DSKx_FXtYXJuQzKdrtXmeAzDf5'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a5359849'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '10604241932238126'},
        #     {'domain': '.qq.com', 'expiry': 1686033450, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.1267384041.1622937407'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1654473323, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': False, 'value': '0'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688851227064419'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'fqm_pvqid', 'path': '/',
        #      'secure': False, 'value': 'd58f5682-f4c8-4411-a858-8710cdc6684a'},
        #     {'domain': '.qq.com', 'expiry': 1936185134, 'httpOnly': False, 'name': 'iip', 'path': '/', 'secure': False,
        #      'value': '0'},
        #     {'domain': '.qq.com', 'expiry': 1623047850, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.559106266.1622937407'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1622968859, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': False, 'value': '3dgob7a'},
        #     {'domain': '.qq.com', 'expiry': 1927986099, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
        #      'secure': False, 'value': '6023ed002c8bb556'},
        #     {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
        #      'value': 'S3bhckWuUs'},
        #     {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
        #      'value': '2d6863f9df971e2ba68436d700207d7292e6b0c29877c519a264f25bdd90698b'},
        #     {'domain': '.qq.com', 'expiry': 1926845292, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
        #      'secure': False, 'value': '0_5a3d5cb23bc93'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1625553452, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1654496268, 'httpOnly': False,
        #                           'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
        #                           'value': '1622937407,1622960268'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
        #      'secure': False, 'value': '9649238560'}]
        db = shelve.open('./mydbs/cookies')  # 链接数据库
        # db['cookie']=cookies           #将数据写入数据库
        # db.close()                     #关闭数据库
        cookies = db['cookie']  # 从数据库中获取数据
        for cookie in cookies:  ##为什么用循环语句？   因为是一个列表， add_coockies只能用字典格式，之能一个个遍历遍历到数据中
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(2)

    # assert "企业微信" in driver.title
