from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.url, "URL is not contains login"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Form for registration is not presented"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD)
        input_password.send_keys(password)
        input_password_repeat = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_REPEAT)
        input_password_repeat .send_keys(password)
        btn_registered = self.browser.find_element(*LoginPageLocators.BTN_REGISTRATION)
        btn_registered.click()

        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUCCESS_MESSAGE),  \
            "Success message about registration is not presented"
