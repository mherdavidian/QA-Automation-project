import time

from selenium import webdriver
import unittest
from Pages.Login.loginPage import LoginPage
from Pages.Login.passwordPage import PasswordPage
from Pages.NavPage.navPage import ChangeDeliveryLocation
from Pages.NavPage.addAddress import AddAddress
from Pages.NavPage.newAddressInformation import NewAddressInformation
from webdriver_manager.chrome import ChromeDriverManager

class TestSignIn(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.PATH = '../common/Driver/chromedriver.exe'
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()
        cls.driver.implicitly_wait(25)
        cls.loginPage = LoginPage(cls.driver)
        cls.passwordPage = PasswordPage(cls.driver)
        cls.changeDeliveryLocation = ChangeDeliveryLocation(cls.driver)
        cls.addAddress = AddAddress(cls.driver)
        cls.newAddressInformation = NewAddressInformation(cls.driver)

    def test_SignIn(self):
        self.driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

        self.loginPage.fill_username('davidianmher@gmail.com')
        self.loginPage.click_continue_button()

        self.passwordPage.fill_password('mher123456')
        self.passwordPage.click_singIn_button()

        self.changeDeliveryLocation.ChangeLocation()

        self.changeDeliveryLocation.ManageAddressBook()

        self.addAddress.AddNewAddress()

        # self.newAddressInformation.Fill_Country_Region_Drop_Down_Menu()
        #
        # self.newAddressInformation.Fill_Country_Region_Name()

        self.newAddressInformation.Add_Full_Name('Mher Davidian')

        self.newAddressInformation.Add_Phone_Number('123456789')

        self.newAddressInformation.Add_Street_Name('950 Ridge RD C25')

        self.newAddressInformation.Add_Zip_code('19703')

        self.newAddressInformation.Add_City_Name('Claymont')

        self.newAddressInformation.State_List_Button()

        self.newAddressInformation.Add_State_Name()

        self.newAddressInformation.Click_Add_Address_Button()

        time.sleep(5)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()