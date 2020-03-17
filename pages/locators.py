from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")

    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_CONFPASS = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT = (By.CSS_SELECTOR,".product_main h1")
    ADDED_PRODUCT_MSG = (By.CSS_SELECTOR,"#messages > .alert:nth-child(1) strong")
    DISCOUNT_MSG = (By.CSS_SELECTOR,"#messages > .alert:nth-child(2) strong")
    PRICE_IN_BASKET_MSG = (By.CSS_SELECTOR,"#messages > .alert:nth-child(3) strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
