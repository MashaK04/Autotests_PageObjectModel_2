import time
from selenium import webdriver
from pages.registration_page import RegistrationPage

class TestRegistrationPage:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.reg_page = RegistrationPage(self.driver)

    def test_registration(self):
        self.reg_page.open()

        # Заполнение данных
        self.reg_page.enter_firstname("Мария")
        self.reg_page.enter_lastname("Каширина")
        self.reg_page.enter_email("test1@test.ru")
        self.reg_page.reenter_email("test1@test.ru")
        self.reg_page.enter_username("KashirinaMO")
        self.reg_page.enter_password("Test1234!")

        # Выбор даты рождения (15 апреля 2019)
        self.reg_page.select_birthdate(day=15, month=6, year=2019)
        # Выбор пола
        self.reg_page.select_gender(gender='female')

        # Принятие соглашения
        self.reg_page.accept_agreement()

        # Нажатие на кнопку регистрации
        self.reg_page.submit_registration()
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()