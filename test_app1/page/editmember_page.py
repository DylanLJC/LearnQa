from appium.webdriver.common.mobileby import MobileBy

# from test_app.page.addmember_page import AddMemberPage
from appium.webdriver.webdriver import WebDriver

from test_app1.page.base_page import BasePage


class EditMemberPage(BasePage):

    def edit_member(self, name, phoneNumber):
        # input[姓名]
        # input[手机号]
        # click[保存]
        self.find_and_send(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText", name)
        self.find_and_send(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='必填']", phoneNumber)
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='必填']").send_keys(phoneNumber)
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        from test_app1.page.addmember_page import AddMemberPage
        return AddMemberPage(self.driver)
