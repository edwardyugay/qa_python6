# tests/test_faq.py
import pytest
import allure
from page_objects.main_page import MainPage
from test_data import faq_data

@allure.feature("FAQ")
class TestFAQ:
    @pytest.mark.parametrize("data", faq_data)
    def test_faq_answer_display(self, browser, data):
        main_page = MainPage(browser)
        main_page.open()
        with allure.step(f"Нажатие на вопрос с индексом {data['question_index']}"):
            main_page.click_faq_question(data["question_index"])
        with allure.step("Получение текста ответа"):
            answer_text = main_page.get_faq_answer(data["question_index"])
        with allure.step("Проверка соответствия текста ответа"):
            assert data["expected_answer"] in answer_text, (
                f"Для вопроса с индексом {data['question_index']} ожидаемый ответ не найден."
            )
