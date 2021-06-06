"""
 第一步：构造py模型
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_web.po.addMumber_page import AddMemberPage
from test_web.po.base_page import BasePage
from test_web.po.contact_page import ContactPage


class MainPage(BasePage):  # 子类调用父类的实例变量
    # 子类中添加base_url 就是起始的url  #和业务解耦
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_contact(self):
        """
        跳转到通讯录页面
        :return:
        """
        return ContactPage(self.driver)

    def goto_addNumber(self):
        """
        跳转到成员页面
        :return:
        """
        # 添加成员
        self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        #
        return AddMemberPage(self.driver)
