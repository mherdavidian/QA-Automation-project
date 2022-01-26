from Pages.Common.baseClass import BaseClass

class Add_To_Card_Page(BaseClass):
    def __init__(self, driver):
        BaseClass.__init__(self, driver)

    def cart_button(self):
        cartButton = self.custom.custom_find_element(self.locators.cart_button)
        cartButton.click()






