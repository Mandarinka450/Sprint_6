from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION = By.XPATH, './/div[@id="accordion__heading-{}"]' # вопрос
    ANSWER = By.XPATH, './/div[@id="accordion__panel-{}"]' # ответ
    QUESTIONS_SECTION = (By.XPATH, './/div[@class="accordion"]') # раздел с вопросами
