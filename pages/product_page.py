from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_add_to_card (self):
        add_cart = self.browser.find_element(*ProductPageLocators.ADD_CART)
        add_cart.click()
    
    def should_be_same_price(self):
        self.text_price = self.browser.find_element(*ProductPageLocators.PRICE_TEXT)
        self.cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE)
        text_price = self.text_price.text
        cart_price = self.cart_price.text
        assert text_price == cart_price, "Different price"
        
    def should_be_same_item_name(self):
        self.text_cart = self.browser.find_element(*ProductPageLocators.CART_TEXT)
        self.cart_name = self.browser.find_element(*ProductPageLocators.CART_NAME)
        text_cart = self.text_cart.text
        cart_name = self.cart_name.text
        assert text_cart == cart_name, "Different name"  
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
    
    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Message is not dissapeared, but should be"
       
    