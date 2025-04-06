from selenium.webdriver.common.by import By
from helper import wait_for_element_clickable

class MainPage:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.BASE_URL)

    def click_faq_question(self, question_index):
        # Кнопка вопроса имеет id вида "accordion__heading-{index}"
        question_locator = (By.ID, f"accordion__heading-{question_index}")
        wait_for_element_clickable(self.driver, question_locator).click()

    def get_faq_answer(self, question_index):
        # Ответ находится в элементе с id "accordion__panel-{index}"
        answer_locator = (By.ID, f"accordion__panel-{question_index}")
        element = wait_for_element_clickable(self.driver, answer_locator)
        return element.text

    def click_scooter_logo(self):
        # Логотип Самоката для возврата на главную страницу
        logo_locator = (By.ID, "scooterLogo")
        wait_for_element_clickable(self.driver, logo_locator).click()

    def click_yandex_logo(self):
        # Логотип Яндекса – открывается в новом окне
        logo_locator = (By.ID, "yandexLogo")
        wait_for_element_clickable(self.driver, logo_locator).click()
