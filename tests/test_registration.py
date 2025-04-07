import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.registration_page import RegistrationPage


class TestRegistrationPage:
    def setup_method(self):
        self.reg_page = RegistrationPage(self.driver)
        self.driver.delete_all_cookies()

    def test_registration(self):
        self.reg_page.open()

        # Заполнение данных
        self.reg_page.enter_firstname("Мария")
        self.reg_page.enter_lastname("Каширина")
        self.reg_page.enter_email("test@test.ru")
        self.reg_page.reenter_email("test@test.ru")
        self.reg_page.enter_username("test_user")
        self.reg_page.enter_password("Test1234!")

        # Выбор даты рождения (15 апреля 2019)
        self.reg_page.select_birthdate(day=15, month="April", year=2019)

        # Выбор пола
        self.reg_page.select_gender(gender='female')

        # Принятие соглашения
        self.reg_page.accept_agreement()

        # Дополнительные действия (например, нажатие кнопки регистрации)
        # register_button = ("xpath", "//button[contains(text(),'Register')]")
        # self.reg_page.click(register_button)

        # Проверка успешной регистрации
        # success_message = ("xpath", "//div[contains(text(),'Registration successful')]")
        # assert self.reg_page.is_displayed(success_message, timeout=10)

        time.sleep(3)  # Временная задержка для демонстрации

    def teardown_method(self):
        pass