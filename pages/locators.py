from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BTN_GO_BASKET = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL = (By.XPATH, "//input[@id='id_registration-email']")
    INPUT_PASSWORD = (By.XPATH, "//input[@id='id_registration-password1']")
    INPUT_PASSWORD_REPEAT = (By.XPATH, "//input[@id='id_registration-password2']")
    BTN_REGISTRATION = (By.XPATH, "//button[@name='registration_submit']")
    REGISTRATION_SUCCESS_MESSAGE = (By.XPATH,"//div[@class='alert alert-success  fade in']/div[@class='alertinner wicon']")


class ProductPageLocators():
    PRODUCT_NAME_EXPECTED = (By.TAG_NAME, "h1")
    PRODUCT_PRICE_EXPECTED = (By.CSS_SELECTOR, ".product_main .price_color")
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success strong")
    INFO_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")


class BasketPageLocators():
    BASKET_EMPTY_MESSAGE = (By.XPATH, "//div[@id='content_inner']/p/a")
    ITEMS_IN_BASKET = (By.XPATH, "//form[@id='basket_formset']")

