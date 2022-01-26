from selenium.webdriver.common.by import By

class Locators():
    #loginPage
    login_field_box = (By.ID, 'ap_email')
    continue_button = (By.CLASS_NAME, 'a-button-input')

    #passwordPage
    password_field_box = (By.ID, 'ap_password')
    singin_button = (By.ID, 'signInSubmit')

    #searchPage
    search_field_box = (By.ID, 'twotabsearchtextbox')
    search_button = (By.ID, 'nav-search-submit-button')

    #SearchResultFilter
    custom_review_filter = (By.ID, 'p_72/1248963011')
    price_deals_filter = (By.ID, 'p_36/1253562011')

    #productPage
    # selected_product = (By.CLASS_NAME, 'a-size-base-plus a-color-base a-text-normal')
    selected_product = (By.CLASS_NAME, 's-image')
    add_to_card_button = (By.ID, 'add-to-cart-button')

    #CartButton
    cart_button = (By.ID, 'nav-cart-count-container')

    #shoppingCartPage
    select_quantity_button = (By.ID, 'a-autoid-0-announce')

    #selectQuantity
    select_quantity = (By.ID, 'quantity_3')

    #CartDeleteButton
    cart_delete_button = (By.XPATH, "//input[@class = 'a-color-link']")

    # ChangLocation
    change_location_button = (By.ID, 'glow-ingress-block')
    manage_address_book_button = (By.ID, 'GLUXManageAddressLink')

    # AddNewAddress
    add_new_address_field = (By.ID, 'ya-myab-plus-address-icon')

    #FillCountryRegionDropDownMenu
    select_country_region_field_dropdown_menu = (By.ID, 'address-ui-widgets-countryCode')

    # FillNewAddressInformation
    select_country_region = (By.ID, 'address-ui-widgets-countryCode-dropdown-nativeId_14')

    #AddFullName
    add_full_name = (By.ID, 'address-ui-widgets-enterAddressFullName')

    #AddPhoneNumber
    add_phone_number = (By.ID, 'address-ui-widgets-enterAddressPhoneNumber')

    #StreetName
    add_street_name = (By.NAME, 'address-ui-widgets-enterAddressLine1')

    #zipCode
    add_zip_code = (By.ID, 'address-ui-widgets-enterAddressPostalCode')

    #cityName
    add_city_name = (By.ID, 'address-ui-widgets-enterAddressCity')

    #stateListButton
    state_list_button = (By.ID, 'address-ui-widgets-enterAddressStateOrRegion')

    #StateName
    add_state_name = (By.ID, "address-ui-widgets-enterAddressStateOrRegion-dropdown-nativeId_8")

    #clickAddAddressButton
    click_add_address_button = (By.ID, 'address-ui-widgets-form-submit-button')

