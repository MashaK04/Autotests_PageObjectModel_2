from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage(BasePage):
    PAGE_URL = "https://demo.opensource-socialnetwork.org/"

    # Описание полей формы
    FIRSTNAME_FIELD = ("xpath", "//input[@name='firstname']")
    LASTNAME_FIELD = ("xpath", "//input[@name='lastname']")
    EMAIL_FIELD = ("xpath", "//input[@name='email']")
    RE_EMAIL_FIELD = ("xpath", "//input[@name='email_re']")
    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    BIRTHDATE_FIELD = ("xpath", "//input[@name='birthdate']")
    FEMALE_GENDER = ("xpath", "//input[@name='gender' and @value='female']")
    MALE_GENDER = ("xpath", "//input[@name='gender' and @value='male']")
    CHECK_FIELD = ("xpath", "//input[@name='gdpr_agree']")

    # Локаторы для datepicker
    DATEPICKER_YEAR = ("xpath", "//select[@class='ui-datepicker-year']")
    DATEPICKER_MONTH = ("xpath", "//select[@class='ui-datepicker-month']")
    DATEPICKER_DAY = ("xpath", "//td[@data-handler='selectDay']/a")

    def enter_firstname(self, firstname):
        self.type(self.FIRSTNAME_FIELD, firstname)

    def enter_lastname(self, lastname):
        self.type(self.LASTNAME_FIELD, lastname)

    def enter_email(self, email):
        self.type(self.EMAIL_FIELD, email)

    def reenter_email(self, reemail):
        self.type(self.RE_EMAIL_FIELD, reemail)

    def enter_username(self, username):
        self.type(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.type(self.PASSWORD_FIELD, password)

    def select_birthdate(self, day, month, year):
        self.click(self.BIRTHDATE_FIELD)  # Открываем datepicker

        # Выбираем год
        self.select_by_visible_text(self.DATEPICKER_YEAR, str(year))

        # Выбираем месяц (нумерация с 0)
        self.select_by_visible_text(self.DATEPICKER_MONTH,
                                    month if isinstance(month, str) else self._get_month_name(month))

        # Выбираем день
        day_locator = (self.DATEPICKER_DAY[0], f"{self.DATEPICKER_DAY[1]}[.='{day}']")
        self.click(day_locator)

    def select_gender(self, gender='female'):
        if gender.lower() == 'female':
            self.click(self.FEMALE_GENDER)
        else:
            self.click(self.MALE_GENDER)

    def accept_agreement(self):
        self.click(self.CHECK_FIELD)

    def _get_month_name(self, month_num):
        """Конвертирует номер месяца в название"""
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        return months[month_num - 1]