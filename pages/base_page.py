from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.ie.webdriver import WebDriver


class BasePage:
    _PAGE_URL = "https://demo.opensource-socialnetwork.org/"
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self):
        self.driver.get(self._PAGE_URL)

    def type(self, locator, text):
        # Ввод текста в поле
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        # Клик по элементу
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def select_by_visible_text(self, locator, text):
        # Выбор из выпадающего списка по видимому тексту
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        Select(element).select_by_visible_text(text)

    def is_element_present(self, locator):
        # Проверка наличия элемента на странице
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except:
            return False