import pytest
from selenium.webdriver.common.by import By

from test_web.po.base_page import BasePage


class AddMemberPage(BasePage):
    # 抽离变量
    username_ele = (By.ID, "username")

    def add_member(self):
        """
        添加成员操作
        :return:
        """

        # 导入到方法内部解决循环导入问题
        from test_web.po.contact_page import ContactPage
        # 输入姓名，id 手机号码

        # self.driver.find_element(*self.username_ele).send_keys(name)   #这个是引用的self.username_ele  需要对元组元素进行解包*
        #                                                                #不解包(By.ID,"username")，解开包By.ID,"username"
        self.find(self.username_ele).send_keys("啦啦队正")
        # self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("254")
        self.find(By.ID, "memberAdd_acctid").send_keys("254")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("12458741254")
        # 点击保存
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()

        return ContactPage(self.driver)

    def add_member_fail(self, name):
        """
        删除成员操作
        :return:
        """
        # 抽离变量
        # 导入到方法内部解决循环导入问题
        from test_web.po.contact_page import ContactPage
        # 输入姓名，id 手机号码

        self.driver.find_element(By.ID, "username").send_keys(name)  # 这个未经引用的
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("254")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("12458741254")
