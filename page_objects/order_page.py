import time

from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from page_objects.base_page import BasePage


class OrderPage(BasePage):
    def click_to_button_order(self, button_order):
        self.scroll_and_click(button_order)

    def complete_form_personal_data_fields(self, first_name, last_name, address, phone_number):
        self.send_data(OrderPageLocators.FIRST_NAME, first_name)
        self.send_data(OrderPageLocators.LAST_NAME, last_name)
        self.send_data(OrderPageLocators.ADDRESS, address)
        self.click_to_element(OrderPageLocators.STATIONS)
        self.scroll_and_click(OrderPageLocators.STATION_METRO)
        self.send_data(OrderPageLocators.PHONE, phone_number)
        self.click_to_element(OrderPageLocators.BUTTON_NEXT)

    def complete_form_renta_of_scooter_fields(self, comment):
        self.click_to_element(OrderPageLocators.DATE)
        self.click_to_element(OrderPageLocators.NUM_DAY)
        self.click_to_element(OrderPageLocators.RENTA_INPUT)
        self.click_to_element(OrderPageLocators.OPTION)
        self.click_to_element(OrderPageLocators.CHECKBOX_BLACK)
        self.send_data(OrderPageLocators.COMMENT, comment)

    def confirm_order(self):
        self.click_to_element(OrderPageLocators.BUTTON_ORDER)
        self.click_to_element(OrderPageLocators.BUTTON_YES)

    def check_visible_window_completed_order(self):
        modal_window = self.wait_visibility_element(OrderPageLocators.SUCCESS_OREDER_MODAL)
        if modal_window:
            return True
        else:
            return False
