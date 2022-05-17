from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    PRODUCT_NAME_EXPECTED = (By.TAG_NAME, "h1")
    PRODUCT_PRICE_EXPECTED = (By.CSS_SELECTOR, ".product_main .price_color")
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MSG_PRODUCT_NAME_TO_BASKET = (By.CSS_SELECTOR, ".alert-success strong")
    MSG_PRODUCT_PRICE_TO_BASKET= (By.CSS_SELECTOR,".alert-info strong")