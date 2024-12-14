from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_ui_present(self):
        self.should_be_add_to_basket_button()
        self.should_be_item_name()
        self.should_be_item_price()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not present"

    def should_be_item_name(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME), "Item name is not present"

    def should_be_item_price(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_PRICE), "Item price is not present"


    def should_be_added_to_basket_messages(self):
        self.should_be_success_message()
        self.should_be_book_name_in_success_message()
        self.should_be_basket_total_price()
        self.should_be_book_price_in_basket_total_price()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not present"

    def should_be_book_name_in_success_message(self):
        book_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert book_name == success_message, f'{book_name} is not the same as {success_message}'

    def should_be_basket_total_price(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_PRICE), "Basket total price is not present"

    def should_be_book_price_in_basket_total_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        basket_total_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        assert book_price == basket_total_price, f'{book_price} is not the same as {basket_total_price}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear, but should have been"









