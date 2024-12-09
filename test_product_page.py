from .pages.product_page import ProductPage
from .pages.main_page import MainPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()

    product_page = ProductPage(browser, link)
    product_page.should_be_ui_present()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_added_to_basket_messages()





