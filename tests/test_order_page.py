import pytest
import allure
from locators.order_page_locators import OrderPageLocators
from page_objects.order_page import OrderPage
from urls import Urls


class TestsCreateOrder:
    @pytest.mark.parametrize('button_order, first_name, last_name, address, phone_number, comment', [
        (OrderPageLocators.ORDER_BUTTON_TOP, 'Антон', 'Партянкин', 'Цветной бульвар, 97', '+79801899067', 'Оставить у двери'),
        (OrderPageLocators.ORDER_BUTTON_BOTTOM, 'Карина', 'Ефимова', 'Проспект Веселого Арбуза, 12', '+79993406087', 'Отличного настроения')
    ])
    @allure.title('Проверка успешного создания заказа на самокат')
    @allure.description('Заполнение необходимых полей в форме, проверяем, что отображается текст об успешном создании заказа')
    def test_create_success_order(self, driver, button_order, first_name, last_name, address, phone_number, comment):
        order_page = OrderPage(driver, Urls.base_url)
        order_page.open_page()
        success_order_text = order_page.create_order(button_order, first_name, last_name, address, phone_number, comment)
        assert 'Заказ оформлен' in success_order_text
