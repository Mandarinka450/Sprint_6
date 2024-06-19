import time

from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from page_objects.base_page import BasePage


class OrderPage(BasePage):
    def create_order(self, button_order, first_name, last_name, address, phone_number, comment):
        self.scroll_and_click(button_order)
        self.send_data(OrderPageLocators.FIRST_NAME, first_name)
        self.send_data(OrderPageLocators.LAST_NAME, last_name)
        self.send_data(OrderPageLocators.ADDRESS, address)
        self.click_to_element(OrderPageLocators.STATIONS)
        self.scroll_and_click(OrderPageLocators.STATION_METRO)
        self.send_data(OrderPageLocators.PHONE, phone_number)
        self.click_to_element(OrderPageLocators.BUTTON_NEXT)
        self.click_to_element(OrderPageLocators.DATE)
        self.click_to_element(OrderPageLocators.NUM_DAY)
        self.click_to_element(OrderPageLocators.RENTA_INPUT)
        self.click_to_element(OrderPageLocators.OPTION)
        self.click_to_element(OrderPageLocators.CHECKBOX_BLACK)
        self.send_data(OrderPageLocators.COMMENT, comment)
        self.click_to_element(OrderPageLocators.BUTTON_ORDER)
        self.click_to_element(OrderPageLocators.BUTTON_YES)
        success_order_text = self.get_text(OrderPageLocators.SUCCESS_OREDER_TEXT)
        return success_order_text
