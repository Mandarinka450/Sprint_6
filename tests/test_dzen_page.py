from page_objects.dzen_page import DzenPage
import allure
from urls import Urls


class TestsDzenPage:
    @allure.title('Проверка перехода на страницу Яндекс.Дзен')
    @allure.description(
        'Проверяем, что при нажатии на логотип Яндекс просиходит переход на страницу Дзена в новом окне')
    def test_go_to_dzen_page(self, driver):
        dzen_page = DzenPage(driver, Urls.base_url)
        dzen_page.open_page()
        current_url = dzen_page.switch_to_dzen_page()
        assert current_url == Urls.dzen_page
