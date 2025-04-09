# base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_clickable(self, locator, timeout=10):
        """Ожидание, пока элемент по заданному локатору не станет кликабельным."""
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def switch_to_new_window(self, current_window, timeout=10):
        """Переключение на новое окно, которое появилось кроме current_window."""
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > 1)
        for handle in self.driver.window_handles:
            if handle != current_window:
                self.driver.switch_to.window(handle)
                break
