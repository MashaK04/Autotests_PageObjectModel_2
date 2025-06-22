from selenium.webdriver.support.select import Select
import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage(BasePage):
    _PAGE_URL = "https://demo.opensource-socialnetwork.org/"

    # Описание полей формы
    _FIRSTNAME_FIELD = ("xpath", "//input[@name='firstname']")
    _LASTNAME_FIELD = ("xpath", "//input[@name='lastname']")
    _EMAIL_FIELD = ("xpath", "//input[@name='email']")
    _RE_EMAIL_FIELD = ("xpath", "//input[@name='email_re']")
    _USERNAME_FIELD = ("xpath", "//input[@name='username']")
    _PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    _BIRTHDATE_FIELD = ("xpath", "//input[@name='birthdate']")
    _FEMALE_GENDER = ("xpath", "//input[@name='gender' and @value='female']")
    _MALE_GENDER = ("xpath", "//input[@name='gender' and @value='male']")
    _CHECK_FIELD = ("xpath", "//input[@name='gdpr_agree']")
    _SUBMIT_BUTTON = (By.XPATH, "//input[@id='ossn-submit-button']")


    # Локаторы для datepicker
    _DATEPICKER_YEAR = (By.CLASS_NAME, "ui-datepicker-year")
    _DATEPICKER_MONTH = (By.CLASS_NAME, "ui-datepicker-month")
    _DATEPICKER_DAY = (By.XPATH, "//td[@data-handler='selectDay']/a")

    def enter_firstname(self, firstname):
        self.type(self._FIRSTNAME_FIELD, firstname)

    def enter_lastname(self, lastname):
        self.type(self._LASTNAME_FIELD, lastname)

    def enter_email(self, email):
        self.type(self._EMAIL_FIELD, email)

    def reenter_email(self, reemail):
        self.type(self._RE_EMAIL_FIELD, reemail)

    def enter_username(self, username):
        self.type(self._USERNAME_FIELD, username)

    def enter_password(self, password):
        self.type(self._PASSWORD_FIELD, password)

    def select_birthdate(self, day, month, year):
        # Открываем календарь
        self.click(self._BIRTHDATE_FIELD)

        # Ждем появления datepicker
        datepicker = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "ui-datepicker"))
        )

        # Выбиор года
        year_select = Select(datepicker.find_element(By.CLASS_NAME, "ui-datepicker-year"))
        year_select.select_by_visible_text(str(year))

        #Выбор месяца
        month_select = Select(datepicker.find_element(By.CLASS_NAME, "ui-datepicker-month"))
        if isinstance(month, str):
            month_select.select_by_visible_text(month.strip())
        else:
            month_select.select_by_value(str(month - 1))

        # Обновление календаря
        time.sleep(0.5)

        # Выбор дня
        day_element = datepicker.find_element(
            By.XPATH,
            f"//td[@data-handler='selectDay']/a[text()='{day}']"
        )
        day_element.click()


    def select_gender(self, gender='female'):
        if gender.lower() == 'female':
            self.click(self._FEMALE_GENDER)
        else:
            self.click(self._MALE_GENDER)

    def accept_agreement(self):
        self.click(self._CHECK_FIELD)

    def _get_month_name(self, month_num):
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        return months[month_num - 1]

    def submit_registration(self):
        # Нажатие кнопки создания аккаунта
        self.click(self._SUBMIT_BUTTON)