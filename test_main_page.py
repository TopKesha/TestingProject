from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser,link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.two
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):  
    page = MainPage(browser,link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_see_product_in_basket()
    basket_page.should_see_empty_basket_text()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser,link)
    page.open()
    page.should_be_login_link()

def go_to_login_page(browser):
    login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    login_link.click()
    alert = self.browser.switch_to.alert
    alert.accept()