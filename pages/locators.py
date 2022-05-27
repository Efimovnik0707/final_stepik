from selenium.webdriver.common.by import By

class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner  p:nth-child(1)") 
    ITEM_BASKET = (By.CSS_SELECTOR, ".basket-items")
    BASKET_NAME = (By.CSS_SELECTOR, ".page-header h1")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CART_PRICE = (By.CSS_SELECTOR, "div.alert-info > div > p:nth-child(1) > strong")
    PRICE_TEXT = (By.CSS_SELECTOR, "div.alertinner > p:nth-child(1) strong")
    CART_TEXT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    CART_NAME = (By.CSS_SELECTOR, "#content_inner h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) div")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    
    