from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_add_to_card (self):
        add_cart = self.browser.find_element(*ProductPageLocators.ADD_CART)
        add_cart.click()
    
    def should_be_same_price(self):
        self.original_price = self.is_element_present(*ProductPageLocators.ORIGINAL_PRICE)
        self.cart_price = self.is_element_present(*ProductPageLocators.CART_PRICE)
        assert self.original_price == self.cart_price, "Different price"
        
    def should_be_same_item_name(self):
        self.original_name = self.is_element_present(*ProductPageLocators.ORIGINAL_NAME)
        self.cart_name = self.is_element_present(*ProductPageLocators.CART_NAME)
        assert self.original_name == self.cart_name, "Different name"  
    