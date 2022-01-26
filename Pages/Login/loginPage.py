from Pages.Common.baseClass import BaseClass

class LoginPage(BaseClass):
    def __init__(self, driver):
        BaseClass.__init__(self, driver)

    def fill_username(self, username):
        login_Field = self.custom.custom_find_element(self.locators.login_field_box)
        login_Field.clear()
        login_Field.send_keys(username)

    def click_continue_button(self):
        continue_button = self.custom.custom_find_element(self.locators.continue_button)
        continue_button.click()
