import time

from Pages.Common.baseClass import BaseClass

class NewAddressInformation(BaseClass):
    def __init__(self, driver):
        BaseClass.__init__(self, driver)

    # def Fill_Country_Region_Drop_Down_Menu(self):
    #     country_region_field_dropdown_menu = self.custom.custom_find_element(self.locators.select_country_region_field_dropdown_menu)
    #     country_region_field_dropdown_menu.click()
    #
    # def Fill_Country_Region_Name(self):
    #     select_country_region = self.custom.custom_find_element(self.locators.select_country_region)
    #     select_country_region.click()

    def Add_Full_Name(self, username):
        add_full_name = self.custom.custom_find_element(self.locators.add_full_name)
        add_full_name.clear()
        add_full_name.send_keys(username)

    def Add_Phone_Number(self, phoneNumber):
        add_phone_number = self.custom.custom_find_element(self.locators.add_phone_number)
        add_phone_number.clear()
        add_phone_number.send_keys(phoneNumber)

    def Add_Street_Name(self, streetName):
        add_street_name = self.custom.custom_find_element(self.locators.add_street_name)
        add_street_name.clear()
        add_street_name.send_keys(streetName)

    def Add_Zip_code(self, postalCode):
        add_zip_code = self.custom.custom_find_element(self.locators.add_zip_code)
        add_zip_code.clear()
        add_zip_code.send_keys(postalCode)

    def Add_City_Name(self, cityName):
        add_city_name = self.custom.custom_find_element(self.locators.add_city_name)
        add_city_name.clear()
        add_city_name.send_keys(cityName)

    def State_List_Button(self):
        state_list_button = self.custom.custom_find_element(self.locators.state_list_button)
        state_list_button.click()

    def Add_State_Name(self):
        select_state = self.custom.custom_find_element(self.locators.add_state_name)
        select_state.click()

    def Click_Add_Address_Button(self):
        address_button = self.custom.custom_find_element(self.locators.click_add_address_button)
        address_button.click()

