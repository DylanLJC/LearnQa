from selenium.webdriver.common.by import By

from test_web.po.addMumber_page import AddMemberPage
from test_web.po.base_page import BasePage


class ContactPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        return AddMemberPage(self.driver)

    def goto_member_list(self):
        """
        获取成员列表
        :return:返回用于断言的信息
        """
        ele = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        # 通过列表推导式获取列表数据信息
        name_list = [i.text for i in ele]
        print(name_list)
        return name_list
