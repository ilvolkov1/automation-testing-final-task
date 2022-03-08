from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_cart(self):
        add_to_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_btn.click()

    def check_if_name_is_correct(self):
        assert self.get_page_element(*ProductPageLocators.BOOK_NAME).text == self.get_page_element(*ProductPageLocators.MESSAGE_BOOK_NAME).text, "Book names are not the same"
        #print(self.get_page_element(*ProductPageLocators.BOOK_NAME).text)
        #print(self.get_page_element(*ProductPageLocators.MESSAGE_BOOK_NAME).text)

    def check_if_price_is_correct(self):
        assert self.get_page_element(*ProductPageLocators.BOOK_PRICE).text== self.get_page_element(*ProductPageLocators.MESSAGE_BOOK_PRICE).text, "Book prices are not the same"
        #print(self.get_page_element(*ProductPageLocators.BOOK_PRICE).text)
        #print(self.get_page_element(*ProductPageLocators.MESSAGE_BOOK_PRICE).text)