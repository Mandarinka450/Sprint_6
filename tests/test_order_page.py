import pytest
import allure

from data_order import DataOrder
from locators.order_page_locators import OrderPageLocators
from page_objects.order_page import OrderPage
from urls import Urls


class TestsCreateOrder:
    @pytest.mark.parametrize('button_order, first_name, last_name, address, phone_number, comment', [
        (OrderPageLocators.ORDER_BUTTON_TOP, DataOrder.first_order['first_name'], DataOrder.first_order['last_name'],
         DataOrder.first_order['address'], DataOrder.first_order['phone'], DataOrder.first_order['comment']),
        (OrderPageLocators.ORDER_BUTTON_BOTTOM, DataOrder.second_order['first_name'],
         DataOrder.second_order['last_name'], DataOrder.second_order['address'],
         DataOrder.second_order['phone'], DataOrder.second_order['comment'])
    ])
    @allure.title('Проверка успешного создания заказа на самокат')
    @allure.description('Заполнение необходимых полей в форме, проверяем, что отображается текст об успешном создании '
                        'заказа')
    def test_create_success_order(self, driver, button_order, first_name, last_name, address, phone_number, comment):
        order_page = OrderPage(driver, Urls.base_url)
        order_page.open_page()
        order_page.click_to_button_order(button_order)
        order_page.complete_form_personal_data_fields(first_name, last_name, address, phone_number)
        order_page.complete_form_renta_of_scooter_fields(comment)
        order_page.confirm_order()
        visible_modal_window = order_page.check_visible_window_completed_order()
        assert visible_modal_window == True
