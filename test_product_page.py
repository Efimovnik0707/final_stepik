from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest

@pytest.mark.skip
@pytest.mark.parametrize('link', ['offer0', 'offer1', 'offer2', 'offer3', 'offer4',
                                  'offer5', 'offer6', pytest.param("offer7", marks=pytest.mark.xfail), 'offer8', 'offer9'])
def test_guest_can_add_product_to_basket(browser,link):
     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={link}"
     page = MainPage(browser, link)   
     page.open()                             
     product_page = ProductPage(browser, browser.current_url) 
     product_page.should_add_to_card ()
     product_page.solve_quiz_and_get_code ()
     time.sleep (5)
     product_page.should_be_same_price ()
     product_page.should_be_same_item_name ()
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.skip    
def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page ()
    login_page = LoginPage(browser, browser.current_url) 
    login_page.should_be_login_page
@pytest.mark.skip    
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket (browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)   
    page.open()                             
    product_page = ProductPage(browser, browser.current_url) 
    product_page.should_add_to_card ()
    product_page.should_not_be_success_message ()
     
@pytest.mark.skip
def test_guest_cant_see_success_message (browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)   
    page.open()                             
    product_page = ProductPage(browser, browser.current_url) 
    product_page.should_not_be_success_message ()
@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket (browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)   
    page.open()                             
    product_page = ProductPage(browser, browser.current_url) 
    product_page.should_add_to_card ()
    product_page.should_dissapear_of_success_message ()



def test_guest_cant_see_product_in_basket_opened_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_basket_page ()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page ()
    basket_page.should_be_empty_basket ()
