from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time
import pytest


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
     

   



     

