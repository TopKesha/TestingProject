from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_page(self):
        assert "basket" in self.browser.current_url, "Basket is not found in current url"
    
    def should_not_see_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Product in basket is presented, but should not be"

    def should_see_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET)
   
