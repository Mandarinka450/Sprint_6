import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('Открытие браузера')
    def open_page(self):
        self.driver.get(self.url)

    @allure.step('Нахождение элемента по локатору')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Ожидание на странице элемента по локатору')
    def wait_visibility_element(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))

    @allure.step('Нажатие на элемент')
    def click_to_element(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Получение текста из элемента')
    def get_text(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator)).text

    @allure.step('Скролл до нужного элемента')
    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Получение текущего урл страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переход на новую активную вкладку')
    def switch_to_new_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Удаление элемента с куками')
    def delete_element_cookie(self):
        self.driver.execute_script('document.getElementsByClassName("App_CookieConsent__1yUIN")[0].remove();')

    @allure.step('Задать формат для локаторов')
    def format_locators(self, locator_question, number):
        method, locator = locator_question
        locator = locator.format(number)
        return method, locator

    @allure.step('Отправление необходимых данных в форме')
    def send_data(self, locator, value):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator)).send_keys(value)

    @allure.step('Шаг: скролл до элемента и нажатие по нему')
    def scroll_and_click(self, locator):
        self.scroll_to_element(locator)
        self.click_to_element(locator)
