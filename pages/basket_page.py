from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_name()  
    
        
    def should_be_basket_name(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_NAME), "This is not basket"    

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "'basket' not in current url" # +

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket have some products" # +
        
    def should_not_be_item_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_BASKET), \
        "Item present, but should not be"

    
        
