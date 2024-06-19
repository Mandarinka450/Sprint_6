from selenium.webdriver.common.by import By
import random


class OrderPageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, './/div[@class="Header_Nav__AGCXC"]/button[contains(text(), "Заказать")]') # кнопка Заказать в верхней части страницы
    ORDER_BUTTON_BOTTOM = (By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button[contains(text(), "Заказать")]') # кнопка Заказать в нижней части страницы
    FIRST_NAME = (By.XPATH, './/input[@placeholder= "* Имя"]') # инпут с вводом имени
    LAST_NAME = (By.XPATH, './/input[@placeholder= "* Фамилия"]') # инпут с вводом фамилии
    ADDRESS = (By.XPATH, './/input[@placeholder= "* Адрес: куда привезти заказ"]')  # инпут с вводом адреса
    STATIONS = (By.XPATH, './/input[@placeholder= "* Станция метро"]')  # инпут с выбором станции метро
    STATION_METRO = (By.XPATH, f'.//li[@data-value= "{random.randint(8, 100)}"]')  # строка с определенной станцией метро
    PHONE = (By.XPATH, './/input[@placeholder= "* Телефон: на него позвонит курьер"]')  # инпут с вводом номера телефона
    BUTTON_NEXT = (By.XPATH, './/button[contains(text(), "Далее")]')  # кнопка Далее
    DATE = (By.XPATH, './/input[@placeholder= "* Когда привезти самокат"]')  # инпут с вводом даты
    NUM_DAY = (By.XPATH, './/div[contains(text(), "25")]')  # 25 июня день
    RENTA_INPUT = (By.XPATH, './/div[contains(text(), "Срок аренды")]')  # инпут с выбором срока аренды
    OPTION = (By.XPATH, './/div[contains(text(), "двое суток")]') # выбор из списка
    CHECKBOX_BLACK = (By.XPATH, './/input[@id="black"]') # чек-бокс с выбором ответа "черный жемчуг"
    COMMENT = (By.XPATH, './/input[@placeholder= "Комментарий для курьера"]') # инпут с вводом комментария
    BUTTON_ORDER = (By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[contains(text(), "Заказать")]')  # кнопка Заказать
    BUTTON_YES = (By.XPATH, './/button[contains(text(), "Да")]')  # кнопка Да
    SUCCESS_OREDER_TEXT = (By.XPATH, './/div[contains(text(), "Заказ оформлен")]') # текст успешного заказа



