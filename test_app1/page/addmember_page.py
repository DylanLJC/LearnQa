from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_app1.page.base_page import BasePage


class AddMemberPage(BasePage):

    def click_addmember_menual(self):
        # click[手动输入添加]

        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        from test_app1.page.editmember_page import EditMemberPage
        return EditMemberPage(self.driver)

    def get_tip(self):
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute("text")
        return result
