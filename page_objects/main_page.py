# page_objects/main_page.py
from selenium.webdriver.common.by import By
from base_page import BasePage
from urls import BASE_URL

class MainPage(BasePage):
    # Локаторы вынесены как атрибуты
    FAQ_QUESTION_TEMPLATE = "accordion__heading-{}"
    FAQ_ANSWER_TEMPLATE = "accordion__panel-{}"
    SCOOTER_LOGO = (By.ID, "scooterLogo")
    YANDEX_LOGO = (By.ID, "yandexLogo")

    def open(self):
        self.driver.get(BASE_URL)

    def click_faq_question(self, question_index):
        locator = (By.ID, self.FAQ_QUESTION_TEMPLATE.format(question_index))
        self.wait_for_element_clickable(locator).click()

    def get_faq_answer(self, question_index):
        locator = (By.ID, self.FAQ_ANSWER_TEMPLATE.format(question_index))
        return self.wait_for_element_clickable(locator).text

    def click_scooter_logo(self):
        self.wait_for_element_clickable(self.SCOOTER_LOGO).click()

    def click_yandex_logo(self):
        self.wait_for_element_clickable(self.YANDEX_LOGO).click()
