from Pages.Common.baseClass import BaseClass

class SearchResultFilter(BaseClass):
    def __init__(self, driver):
        BaseClass.__init__(self, driver)

    def Custom_Review_Filter(self):
        custom_review = self.custom.custom_find_element(self.locators.custom_review_filter)
        custom_review.click()

    def Price_Deals_Filter(self):
        price_deals = self.custom.custom_find_element(self.locators.price_deals_filter)
        price_deals.click()



