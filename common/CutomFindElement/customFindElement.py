from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class customFindElement():
    def __init__(self, driver):
        self.driver = driver

    def custom_find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((locator)))
        except:
            print('sorry')
        return element


# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class customFindElement():
#     def __init__(self, driver):
#         self.driver = driver
#
#     def custom_find_element(self, locator):
#         try:
#             element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
#         except NoSuchElementException:
#             pass
#         return element



