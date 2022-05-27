from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        
    def register_new_user(self, email, password):
        self.email = email
        self.password = password
        self.input_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        self.input_email.send_keys (email)
        self.input_password1 = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        self.input_password1.send_keys (password)
        self.input_password2 = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        self.input_password2.send_keys (password)
        button = self.browser.find_element(*LoginPageLocators.BUTTON_LOGIN)
        button.click()
        