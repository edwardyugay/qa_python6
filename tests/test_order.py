import pytest
import allure
from page_objects.order_page import OrderPage
from page_objects.main_page import MainPage
from test_data import order_data
from helper import switch_to_new_window

@allure.feature("Заказ")
class TestOrder:
    @pytest.mark.parametrize("order_info", order_data)
    def test_order_flow(self, browser, order_info):
        order_page = OrderPage(browser)
        order_page.open()
        with allure.step("Нажатие на верхнюю кнопку 'Заказать'"):
            order_page.click_order_button(position="top")
        with allure.step("Заполнение формы заказа"):
            order_page.fill_order_form(order_info)
        with allure.step("Отправка заказа"):
            order_page.submit_order()
        with allure.step("Проверка подтверждения заказа"):
            confirmation_text = order_page.get_order_confirmation()
            assert "Заказ оформлен" in confirmation_text, "Сообщение о подтверждении заказа отсутствует."

    @allure.feature("Логотипы")
    def test_logo_navigation(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        original_window = browser.current_window_handle

        with allure.step("Переход на главную страницу через логотип 'Самоката'"):
            main_page.click_scooter_logo()
            assert browser.current_url == MainPage.BASE_URL, "Переход по логотипу 'Самоката' некорректен."

        with allure.step("Переход на главную страницу Яндекса через логотип"):
            browser.get(MainPage.BASE_URL)
            main_page.click_yandex_logo()
            switch_to_new_window(browser, original_window)
            expected_url_part = "dzen.ru"
            assert expected_url_part in browser.current_url, "Переход по логотипу Яндекса некорректен."
