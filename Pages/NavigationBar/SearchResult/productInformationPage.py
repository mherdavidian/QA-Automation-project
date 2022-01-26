from Pages.Common.baseClass import BaseClass

class SearchResultProductPage(BaseClass):
    def __init__(self, driver):
        BaseClass.__init__(self, driver)

    def click_add_to_card_button(self):
        AddToCardButton = self.custom.custom_find_element(self.locators.add_to_card_button)
        AddToCardButton.click()

