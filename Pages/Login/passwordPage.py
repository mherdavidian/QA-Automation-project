from Pages.Common.baseClass import BaseClass

class PasswordPage(BaseClass):
    def __init__(self, driver):
        BaseClass.__init__(self, driver)

    def fill_password(self, password):
        password_Field = self.custom.custom_find_element(self.locators.password_field_box)
        password_Field.clear()
        password_Field.send_keys(password)

    def click_singIn_button(self):
        # signIn_button = self.driver.find_element(self.locators.singin_button[0], self.locators.singin_button[1])
        signIn_button = self.custom.custom_find_element(self.locators.singin_button)
        signIn_button.click()

