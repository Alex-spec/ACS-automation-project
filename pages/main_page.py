from base.base_methods import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(Base):
    """ Класс содержащий локаторы и методы для страницы Авторизации"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = 'https://acscustom.com/uk'

    # LOCATORS
    login_icon = "//img[@alt='profile picture']"
    login_button = "//button[p[contains(text(), 'Login')]]"
    input_email = "//input[@type='email']"
    input_password = "//input[@placeholder='Password']"
    button_sign_in = "//span[contains(text(), 'Sign in')]"
    products_button = "//span[contains(text(), 'Products')]"
    profile_name = "//p[@class='font-semibold']" # локатор для проверки авторизации

    # GETTERS
    def get_login_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_icon)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_input_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_email)))

    def get_input_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_password)))

    def get_button_sign_in(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_sign_in)))

    def get_products_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.products_button)))

    def get_profile_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_name)))
    # ACTIONS
    def click_login_icon(self):
        self.get_login_icon().click()
        print("Кликнули на иконку профиля")\

    def click_login_button(self):
        self.get_login_button().click()
        print("Кликнули на иконку Login")

    def input_email_form(self, user_name):
        self.get_input_email().send_keys(user_name)
        print("Ввели почту пользователя")

    def input_password_form(self, password):
        self.get_input_password().send_keys(password)
        print("Ввели пароль пользователя")

    def click_button_sign_in(self):
        self.get_button_sign_in().click()
        print("Кликнули на иконку Sign In")

    def click_products_button(self):
        self.get_products_button().click()
        print("Кликнули на иконку Products")


    # METHODS
    def authorization(self):
        """ Авторизация в системе"""
        self.driver.get(self.url) # открытие требуемой url
        self.driver.maximize_window()
        self.click_login_icon()
        self.click_login_button()
        self.input_password_form("qweQwe123#")
        self.input_email_form("alexyankovskio@gmail.com")
        self.click_button_sign_in()
        self.assert_word_sign_in(self.get_profile_name(), "Alex QA")

    def authorization_second(self):
        """ Авторизация в системе"""
        self.driver.get(self.url) # открытие требуемой url
        self.driver.maximize_window()
        self.click_login_icon()
        self.click_login_button()
        self.input_password_form("qweQwe123#")
        self.input_email_form("alexqamiroshkin@gmail.com")
        self.click_button_sign_in()
        self.assert_word_sign_in(self.get_profile_name(), "Alex Yankovsky")


