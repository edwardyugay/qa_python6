from selenium.webdriver.common.by import By
from helper import wait_for_element_clickable


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        # Начинаем с главной страницы
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    def click_order_button(self, position="top"):
        """
        position: "top" или "bottom"
        """
        if position == "top":
            locator = (By.ID, "orderButton")
        else:
            locator = (By.ID, "orderButtonBottom")
        wait_for_element_clickable(self.driver, locator).click()

    def fill_order_form(self, order_info):
        # Заполнение личных данных
        wait_for_element_clickable(self.driver, (By.ID, "firstName")).send_keys(order_info["first_name"])
        wait_for_element_clickable(self.driver, (By.ID, "lastName")).send_keys(order_info["last_name"])
        wait_for_element_clickable(self.driver, (By.ID, "address")).send_keys(order_info["address"])
        wait_for_element_clickable(self.driver, (By.ID, "metro")).send_keys(order_info["metro"])
        wait_for_element_clickable(self.driver, (By.ID, "phone")).send_keys(order_info["phone"])

        # Переход к следующему этапу заполнения
        wait_for_element_clickable(self.driver, (By.ID, "nextButton")).click()

        # Заполнение данных доставки
        wait_for_element_clickable(self.driver, (By.ID, "orderDate")).send_keys(order_info["order_date"])
        wait_for_element_clickable(self.driver, (By.ID, "rentalPeriod")).click()
        # Для простоты выбираем вариант "сутки" из выпадающего списка
        wait_for_element_clickable(self.driver, (By.XPATH, "//div[@id='rentalPeriod']//option[@value='сутки']")).click()
        wait_for_element_clickable(self.driver, (By.ID, "comment")).send_keys(order_info["comment"])

    def submit_order(self):
        # Финальное подтверждение заказа
        wait_for_element_clickable(self.driver, (By.ID, "orderSubmit")).click()

    def get_order_confirmation(self):
        # Модальное окно подтверждения заказа имеет id "orderConfirmation"
        confirmation_locator = (By.ID, "orderConfirmation")
        element = wait_for_element_clickable(self.driver, confirmation_locator)
        return element.text
