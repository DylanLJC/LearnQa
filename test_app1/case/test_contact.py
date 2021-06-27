from appium import webdriver
from faker import Faker

from test_app1.page.app import App


class TestConteact:
    def setup_class(self):
        self.fake = Faker("zh_CN")
        self.app = App()  # 直接在这里初始化app

    def setup(self):
        # 去掉这里的初始化，放在class中的初始化
        # # driver的初始化，app启动
        # self.app = App()
        # self.app.start() #方法一，调用接口
        self.main = self.app.start()  # 方法二，通过

    def teardown(self):
        self.app.back()
        # 每次执行完测试用例就back一次

    def teardown_class(self):  # 最后进行关闭
        self.app.stop()

    def test_addcontact(self):
        name = self.fake.name()
        phoneNumber = self.fake.phone_number()
        # self.app.goto_main() #方法一，调用接口
        result1 = self.main.goto_main().goto_addresslist(). \
            goto_addmember().click_addmember_menual(). \
            edit_member(name, phoneNumber).get_tip()
        assert result1 == "添加成功"

    def test_addcontact2(self):
        name = self.fake.name()
        phoneNumber = self.fake.phone_number()
        # self.app.goto_main() #方法一，调用接口
        result = self.main.goto_main().goto_addresslist(). \
            goto_addmember().click_addmember_menual(). \
            edit_member(name, phoneNumber).get_tip()
        assert result == "添加成功"
