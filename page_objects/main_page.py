import time

from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):
    def get_answer_text(self, number):
        self.wait_visibility_element(BasePageLocators.TEXT_SCOOTER)
        self.delete_element_cookie()
        self.scroll_to_element(MainPageLocators.QUESTIONS_SECTION)
        question = self.format_locators(MainPageLocators.QUESTION, number)
        answer = self.format_locators(MainPageLocators.ANSWER, number)
        self.click_to_element(question)
        answer_text = self.get_text(answer)
        return answer_text

