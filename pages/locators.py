from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ORIGINAL_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ORIGINAL_NAME = (By.CSS_SELECTOR, ".breadcrumb .active ")
    CART_PRICE = (By.CSS_SELECTOR, "div.alert-info > div > p:nth-child(1) > strong")
    CART_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")