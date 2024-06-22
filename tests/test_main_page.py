import pytest
import allure

from data_answer import DataAnswer
from page_objects.main_page import MainPage
from urls import Urls


class TestQuestions:
    @pytest.mark.parametrize('number, answer',
                             [
                                 (DataAnswer.answer_one['id'], DataAnswer.answer_one['answer']),
                                 (DataAnswer.answer_two['id'], DataAnswer.answer_two['answer']),
                                 (DataAnswer.answer_three['id'], DataAnswer.answer_three['answer']),
                                 (DataAnswer.answer_four['id'], DataAnswer.answer_four['answer']),
                                 (DataAnswer.answer_five['id'], DataAnswer.answer_five['answer']),
                                 (DataAnswer.answer_six['id'], DataAnswer.answer_six['answer']),
                                 (DataAnswer.answer_seven['id'], DataAnswer.answer_seven['answer']),
                                 (DataAnswer.answer_eight['id'], DataAnswer.answer_eight['answer'])
                             ])
    @allure.title('Проверка получения ответа на конкретный вопрос')
    @allure.description(
        'Проверяем, что определенному вопросу соответствует определенный ответ')
    def test_check_questions_get_answers(self, driver, number, answer):
        main_page = MainPage(driver, Urls.base_url)
        main_page.open_page()
        main_page.scroll_and_click_to_question(number)
        text = main_page.get_answer_text(number)
        assert text == answer

