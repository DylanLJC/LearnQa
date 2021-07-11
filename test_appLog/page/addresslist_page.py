from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appLog.page.addmember_page import AddMemberPage
from test_appLog.page.base_page import BasePage


class AddressListPage(BasePage):
    addresslist_element = (MobileBy.XPATH, "//*[@text='添加成员']")

    def goto_addmember(self):
        # click[添加成员]
        self.find_and_click(*self.addresslist_element)
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        return AddMemberPage(self.driver)
