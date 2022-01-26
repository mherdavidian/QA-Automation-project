from Pages.Common.baseClass import BaseClass

class HomePage(BaseClass):
    def __init__(self, driver):
        BaseClass.__init__(self, driver)

    def search_Product_Name(self, productName):
        search_field = self.driver.find_element(self.locators.search_field_box[0], self.locators.search_field_box[1])
        search_field.clear()
        search_field.send_keys(productName)

    def click_search_button(self):
        search_button = self.driver.find_element(self.locators.search_button[0], self.locators.search_button[1])
        search_button.click()
