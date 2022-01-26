from Pages.Common.baseClass import BaseClass

class AddAddress(BaseClass):
    def __init__(self, driver):
        BaseClass.__init__(self, driver)

    def AddNewAddress(self):
        add_new_address = self.custom.custom_find_element(self.locators.add_new_address_field)
        add_new_address.click()


