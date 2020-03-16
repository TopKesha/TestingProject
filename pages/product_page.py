from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
  
    def should_add_to_basket(self):
        self.should_be_add_button()
        basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket.click()
        self.solve_quiz_and_get_code()
        self.should_be_same_product_in_added_product_message()
        self.should_be_message_about_success_discount()
        self.should_be_same_item_price_and_price_in_basket()

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Button Add to busket isn't found"

    def should_be_same_product_in_added_product_message(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT)
        added_product_msg = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_MSG)
        assert product.text in added_product_msg.text, "Product name and added product message do not match"

    def should_be_message_about_success_discount(self):
        discount = self.browser.find_element(*ProductPageLocators.DISCOUNT_MSG)
        success = "Deferred benefit offer"
        assert success in discount.text, "There is no 'Deferred benefit offer' in discount message"

    def should_be_same_item_price_and_price_in_basket(self):
        basket_value_msg = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET_MSG)
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        assert item_price.text in basket_value_msg.text, f"Item price and price in basket do not match \n expected {item_price.text}, got {basket_value_msg.text}"