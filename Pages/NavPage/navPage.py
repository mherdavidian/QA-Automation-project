from Pages.Common.baseClass import BaseClass

class ChangeDeliveryLocation(BaseClass):
    def __init__(self, driver):
        BaseClass.__init__(self, driver)

    def ChangeLocation(self):
        change_location = self.custom.custom_find_element(self.locators.change_location_button)
        change_location.click()

    def ManageAddressBook(self):
        manage_address_book = self.custom.custom_find_element(self.locators.manage_address_book_button)
        manage_address_book.click()
