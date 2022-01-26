from Pages.Common.baseClass import BaseClass

class ShoppingCartPage(BaseClass):
    def __init__(self, driver):
        BaseClass.__init__(self, driver)

    def SelectQuantityButton(self):
        quantityButton = self.custom.custom_find_element(self.locators.select_quantity_button)
        quantityButton.click()


    def Select_Quantity(self):
        selectQuantity = self.custom.custom_find_element(self.locators.select_quantity)
        selectQuantity.click()

    def Delete_Button(self):
        deleteButton = self.custom.custom_find_element(self.locators.cart_delete_button)
        deleteButton.click()








