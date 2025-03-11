import time

from base.base_methods import Base
from selenium.webdriver.common.by import By
from pages.products_page import ProductPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage(Base):
    """ Класс содержащий локаторы и методы для страницы Авторизации"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def assert_price_cart_page(self, word, result):
        """Проверка что стоимость совпадает"""
        value_word = word
        assert value_word == result
        print("--Стоимость в корзине и на странице cart совпадает--")

    def assert_price_checkout_total_page(self, word, result):
        """Проверка что стоимость совпадает"""
        value_word = word
        assert value_word == result
        print("--Общая стоимость на странице чекаут совпадает--")

    def assert_final_url(self, partial_url):
        """Проверка, что текущий URL содержит заданную строку"""
        WebDriverWait(self.driver, 10).until(EC.url_contains(partial_url))
        current_url = self.driver.current_url
        print(f"Ожидается '{partial_url}' в '{current_url}'")
        assert partial_url in current_url, f"!URL не совпадает. Ожидается: '{partial_url}', Текущий результат: '{current_url}'"

    # LOCATORS
    cart_total_price = "//p[@class='text-xl font-semibold']/span"
    cart_proceed_button = "//button[@class='py-2 flex items-center transition-3 h-[40px] hover:opacity-75 bg-acs-orange text-white flex items-center justify-center w-full hover:opacity-75 px-4']"
    left_checkout_total_price = "//span[@class='text-[#FF640D]']"
    right_checkout_total_price = "//*/div/div/div[1]/main/div[2]/div[2]/div/div/div[2]/div/div[6]/div/div[1]/p[2]"
    button_next_to_payment = "//span[contains(text(), ' Next to Payment ')]"

    # GETTERS
    def get_cart_total_price(self):
        value_cart_total_price = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_total_price))).text
        pure_value_cart_total_price = value_cart_total_price.replace('£', '').replace(',', '')
        # Общая стоимость в корзине перед чекаутом
        return float(pure_value_cart_total_price)

    def get_cart_proceed_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_proceed_button)))

    def get_left_checkout_total_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.left_checkout_total_price))).text

    def get_right_checkout_total_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.right_checkout_total_price))).text

    def get_button_next_to_payment(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_next_to_payment)))

    # ACTIONS
    def assertion_prices_product_and_checkout_pages(self, get_total_price, get_cart_total_price):
        # Проверка, что цены совпадают
        assert get_total_price == get_cart_total_price, \
            f"!Цены не совпадают. Цена в корзине: {get_total_price}, цена на чекаут странице: {get_cart_total_price}"

        # Если цены совпали, выводим сообщение
        print(f"--Цены совпадают: {get_total_price} == {get_cart_total_price}--")

    def click_cart_proceed_button(self):
        self.get_cart_proceed_button().click()
        print("Кликаем по кнопке procced")

    def click_get_button_next_to_payment(self):
        self.get_button_next_to_payment().click()
        print("Кликаем по кнопке next to payment")

    # METHODS
    def checkout_page_actions(self):
        self.click_cart_proceed_button()
        self.assert_url("https://acscustom.com/uk/cart")
        self.assert_price_checkout_total_page(self.get_left_checkout_total_price(), self.get_right_checkout_total_price())
        time.sleep(2)
        self.click_get_button_next_to_payment()
        self.assert_final_url("https://www.mollie.com/checkout/select-method/")







