from selenium.webdriver.common.by import By


class DzenPageLocators:
    LOGO_DZEN = (By.XPATH, './/a[@class="Header_LogoYandex__3TSOI"]') # логотип яндекса на странице самоката
    NEWS = (By.XPATH, './/div[contains(text(), "Новости")]') # заголовок с новостями
