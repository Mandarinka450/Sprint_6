from selenium.webdriver.common.by import By


class BasePageLocators:
    TEXT_SCOOTER = (By.XPATH, './/div[contains(text(), "Самокат")]') # текст
