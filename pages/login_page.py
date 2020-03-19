from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login is not found in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL),\
           "Log in form: email input is not presented"   
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS),\
           "Log in: password input is not presented"    
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON),\
           "Log in: log in button is not presented"    

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL),\
           "Registration form: email input is not presented"  
        assert self.is_element_present(*LoginPageLocators.REG_PASS),\
           "Registration form: password input is not presented"   
        assert self.is_element_present(*LoginPageLocators.REG_CONFPASS),\
           "Registration form: confirm password input is not presented"   
        assert self.is_element_present(*LoginPageLocators.REG_BUTTON),\
           "Registration form: register button is not presented"
        
    def register_new_user(self,email,password):
        email_box = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email_box.send_keys(email)

        password_box = self.browser.find_element(*LoginPageLocators.REG_PASS)
        password_box.send_keys(password)
        passconf_box = self.browser.find_element(*LoginPageLocators.REG_CONFPASS)
        passconf_box.send_keys(password)

        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()