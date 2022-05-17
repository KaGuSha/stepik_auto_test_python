from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_items_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
            "Items is not presented in the basket"

    def should_be_message_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "Message Basket is empty is not presented"
        # //div[@id="content_inner"]/p/a

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
            "Items is presented in the basket, but should not be"

    def should_not_be_message_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "Message Basket is empty is presented, but should not be"
        # //div[@id="content_inner"]/p/a
