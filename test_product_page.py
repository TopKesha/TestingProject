from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser,link)
    page.open()
    page.should_add_to_basket()

@pytest.mark.smoke   
@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='Bug with added product name')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser,link)
    page.open()
    page.should_add_to_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser,link)
    page.open()
    page.should_add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser,link)
    page.open()
    page.should_add_to_basket()
    page.should_be_disappeared()

@pytest.mark.one
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.one
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser,link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.two
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):     ##
    page = ProductPage(browser,link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_see_product_in_basket()
    basket_page.should_see_empty_basket_text()
  
def go_to_login_page(browser):
    login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    login_link.click()