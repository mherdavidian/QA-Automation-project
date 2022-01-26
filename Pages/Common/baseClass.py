from Locators.locators import Locators
from common.CutomFindElement.customFindElement import customFindElement

class BaseClass():
    def __init__(self, driver):
        self.driver = driver
        self.locators = Locators
        self.custom = customFindElement(driver)