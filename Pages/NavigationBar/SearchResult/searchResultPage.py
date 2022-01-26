from Pages.Common.baseClass import BaseClass

class searchResultPage(BaseClass):
    def __init__(self, driver):
        BaseClass.__init__(self, driver)

    def click_into_specific_product(self):
        selected_product = self.custom.custom_find_element(self.locators.selected_product)
        selected_product.click()


