from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time


def test_guest_can_add_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_added_to_basket()
    page.amount_should_be_equal_to_price()





