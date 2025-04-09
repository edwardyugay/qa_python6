# page_objects/order_page.py
from selenium.webdriver.common.by import By
from base_page import BasePage
from urls import BASE_URL

class OrderPage(BasePage):
    # Локаторы, вынесенные как атрибуты класса
    ORDER_BUTTON_TOP = (By.ID, "orderButton")
    ORDER_BUTTON_BOTTOM = (By.ID, "orderButtonBottom")
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    ADDRESS_INPUT = (By.ID, "address")
    METRO_INPUT = (By.ID, "metro")
    PHONE_INPUT = (By.ID, "phone")
    NEXT_BUTTON = (By.ID, "nextButton")
    ORDER_DATE_INPUT = (By.ID, "orderDate")
    RENTAL_PERIOD_DROPDOWN = (By.ID, "rentalPeriod")
    RENTAL_PERIOD_OPTION_SUTKI = (By.XPATH, "//div[@id='rentalPeriod']//option[@value='сутки']")
    COMMENT_INPUT = (By.ID, "comment")
    ORDER_SUBMIT_BUTTON = (By.ID, "orderSubmit")
    ORDER_CONFIRMATION_MODAL = (By.ID, "orderConfirmation")

    def open(self):
        self.driver.get(BASE_URL)

    def click_order_button(self, position="top"):
        if position == "top":
            locator = self.ORDER_BUTTON_TOP
        else:
            locator = self.ORDER_BUTTON_BOTTOM
        self.wait_for_element_clickable(locator).click()

    def fill_order_form(self, order_info):
        # Заполнение личных данных
        self.wait_for_element_clickable(self.FIRST_NAME_INPUT).send_keys(order_info["first_name"])
        self.wait_for_element_clickable(self.LAST_NAME_INPUT).send_keys(order_info["last_name"])
        self.wait_for_element_clickable(self.ADDRESS_INPUT).send_keys(order_info["address"])
        self.wait_for_element_clickable(self.METRO_INPUT).send_keys(order_info["metro"])
        self.wait_for_element_clickable(self.PHONE_INPUT).send_keys(order_info["phone"])
        # Переход к данным доставки
        self.wait_for_element_clickable(self.NEXT_BUTTON).click()
        # Заполнение данных доставки
        self.wait_for_element_clickable(self.ORDER_DATE_INPUT).send_keys(order_info["order_date"])
        self.wait_for_element_clickable(self.RENTAL_PERIOD_DROPDOWN).click()
        self.wait_for_element_clickable(self.RENTAL_PERIOD_OPTION_SUTKI).click()
        self.wait_for_element_clickable(self.COMMENT_INPUT).send_keys(order_info["comment"])

    def submit_order(self):
        self.wait_for_element_clickable(self.ORDER_SUBMIT_BUTTON).click()

    def get_order_confirmation(self):
        return self.wait_for_element_clickable(self.ORDER_CONFIRMATION_MODAL).text
