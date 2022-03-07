from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "This is not Login Page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Can't find Login Email text field"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Can't find Login Password text field"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Can't find Register Email text field"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "Can't find Register Password text field"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_CONFIRMATION), \
            "Can't find Register Password Confirmation text field"

