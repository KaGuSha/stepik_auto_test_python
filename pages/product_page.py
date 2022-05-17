from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()

    def check_name_of_product_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_EXPECTED).text
        msg_product_name_in_basket = self.browser.find_element(*ProductPageLocators.MSG_PRODUCT_NAME_TO_BASKET).text

        assert msg_product_name_in_basket in product_name, f" Name of the product in alert {msg_product_name_in_basket}, expected name {product_name}."

    def check_price_of_product_in_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_EXPECTED).text
        msg_product_price_in_basket = self.browser.find_element(*ProductPageLocators.MSG_PRODUCT_PRICE_TO_BASKET).text

        assert msg_product_price_in_basket in product_price, f" Price of the product in alert {msg_product_price_in_basket}, expected ={product_price}."