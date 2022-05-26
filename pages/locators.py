from selenium.webdriver.common.by import By


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