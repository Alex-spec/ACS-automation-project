import time
from base.base_methods import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(Base):
    """ Класс содержащий локаторы и методы для страницы Авторизации"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assert_word_product_page(self, word, result):
        """Проверка значения текста в корзине"""
        value_word = word.text
        assert value_word == result
        print("--Данные в корзине совпадают--")

    def assert_success_product_page(self, word, result):
        """Проверка товар успешно добавлен"""
        value_word = word.text
        assert value_word == result
        print("--Товар успешно добавлен в корзину--")

    url = 'https://acscustom.com/uk/products'

    # LOCATORS
    product_sleep_sound = "(//button[@class='py-2 flex items-center transition-3 h-[40px] hover:opacity-75 bg-acs-orange text-white text-sm flex justify-center w-full xs:w-auto px-4'])[1]"
    radiobutton_left_only = "//input[@id='176']"
    product_dropdown = "//button[@placeholder='Colour']"
    product_neon_orange = "//button[contains(text(), 'Neon Orange +£5')]"
    product_dropdown_plus_button = "//button[@class='border h-[48px] w-[48px] flex items-center justify-center']"
    button_add_to_card = "//img[@src='/icons/cart.svg']"
    product_page_card = "//button[@class='px-5 py-2 relative']"
    product_page_card_bin = "//*/div/div/div[9]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/button"
    product_page_card_proceed = "//button[@class='py-2 flex items-center transition-3 h-[40px] hover:opacity-75 w-full bg-acs-orange text-white font-semibold flex justify-center px-4']"
    product_sleep_sound_name = "//h1[contains(text(), 'SleepSound')]"
    product_neon_orange_name = "//p[contains(text(), 'Neon Orange +£5')]"
    product_success_name ="//p[@class='text-sm font-medium text-green-600']"
    total_price = "//p[@class='text-xl font-semibold']/span"

    # GETTERS
    def get_product_sleep_sound(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_sleep_sound)))

    def get_radiobutton_left_only(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.radiobutton_left_only)))

    def get_product_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_dropdown)))

    def get_product_neon_orange(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_neon_orange)))

    def get_product_dropdown_plus_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_dropdown_plus_button)))

    def get_product_sleep_sound_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_sleep_sound_name)))

    def get_product_neon_orange_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_neon_orange_name)))

    def get_button_add_to_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_add_to_card)))

    def get_product_success_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_success_name)))

    def get_product_page_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_page_card)))

    def get_product_page_card_bin(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_page_card_bin)))

    def get_product_page_card_proceed(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_page_card_proceed)))

    def get_total_price(self):
        value_total_price = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.total_price))).text
        pure_value_total_price = value_total_price.replace('£', '').replace(',', '')
        # Общая стоимость в корзине
        return float(pure_value_total_price)

    # ACTIONS
    def click_product_sleep_sound(self):
        self.get_product_sleep_sound().click()
        print("Добавили продукт Sleep sound")

    def click_radiobutton_left_only(self):
        self.get_radiobutton_left_only().click()
        print("Кликаем на left only radiobutton")

    def click_get_product_dropdown(self):
        self.get_product_dropdown().click()
        print("Кликаем на дропдаун")

    def click_product_neon_orange(self):
        self.get_product_neon_orange().click()
        print("Выбираем вариант neon orange")

    def click_product_dropdown_plus_button(self, times=6):
        for _ in range(times):  # Повторяем клик 6 раз
            self.get_product_dropdown_plus_button().click()
        print(f"Выбираем количество товара для покупки {times} раз")

    def click_product_page_card(self):
        self.get_product_page_card().click()
        print("Кликаем на дропдаун")

    def click_button_add_to_card(self):
        self.get_button_add_to_card().click()
        print("Кликаем по кнопке add to card")

    def click_product_page_card_bin(self):
        self.get_product_page_card_bin().click()
        print("Кликаем по кнопке удаления")

    def click_product_page_card_proceed(self):
        self.get_product_page_card_proceed().click()
        print("Кликаем по кнопке Proceed to checkout")

    # METHODS
    def select_and_add_to_cart(self):
        self.click_product_sleep_sound()
        self.click_radiobutton_left_only()
        self.click_get_product_dropdown()
        self.click_product_neon_orange()
        self.click_product_dropdown_plus_button()
        self.click_button_add_to_card()
        self.click_product_page_card()
        time.sleep(2)
        self.get_total_price()
        self.click_product_page_card_proceed()
        self.assert_url("https://acscustom.com/uk/products/other-products/sleep-sound/")
        self.assert_word_product_page(self.get_product_sleep_sound_name(), "SleepSound")
        self.assert_word_product_page(self.get_product_neon_orange_name(), "Neon Orange +£5")
        self.assert_success_product_page(self.get_product_success_name(), "Success!")








