import time

from selenium import webdriver
from Pages.Login.loginPage import LoginPage
from Pages.Login.passwordPage import PasswordPage
from Pages.Home.homePage import HomePage
from Pages.NavigationBar.SearchResult.searchResultPage import searchResultPage
from Pages.NavigationBar.SearchResult.productInformationPage import SearchResultProductPage
import unittest
from Pages.NavigationBar.CartPage.cartPage import Add_To_Card_Page
from Pages.ShoppingCart.shoppingcart import ShoppingCartPage
from Pages.NavigationBar.SearchResult.searchResultFilter import SearchResultFilter
from webdriver_manager.chrome import ChromeDriverManager


class TestSignIn(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.PATH = '../common/Driver/chromedriver.exe'
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()
        cls.driver.implicitly_wait(10)
        cls.loginPage = LoginPage(cls.driver)
        cls.passwordPage = PasswordPage(cls.driver)
        cls.homePage = HomePage(cls.driver)
        cls.searchResultPage= searchResultPage(cls.driver)
        cls.selectedProductPage = SearchResultProductPage(cls.driver)
        cls.addToCardPage = Add_To_Card_Page(cls.driver)
        cls.shoppingCartPage = ShoppingCartPage(cls.driver)
        cls.searchResultFilter = SearchResultFilter(cls.driver)



    def test_SignIn(self):
        self.driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

        self.loginPage.fill_username('davidianmher@gmail.com')
        self.loginPage.click_continue_button()

        self.passwordPage.fill_password('mher123456')
        self.passwordPage.click_singIn_button()

        self.homePage.search_Product_Name('jenga')
        self.homePage.click_search_button()

        self.searchResultFilter.Price_Deals_Filter()
        time.sleep(2)
        self.searchResultFilter.Custom_Review_Filter()

        self.searchResultPage.click_into_specific_product()

        self.selectedProductPage.click_add_to_card_button()

        self.addToCardPage.cart_button()

        self.shoppingCartPage.SelectQuantityButton()
        self.shoppingCartPage.Select_Quantity()
        self.shoppingCartPage.Delete_Button()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()




