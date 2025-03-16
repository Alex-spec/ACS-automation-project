import time
from pages.main_page import MainPage
from pages.products_page import ProductPage
from pages.checkout_page import CheckoutPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_smoke_test_acs(driver):
    print("Start Test")

    # Создание объекта страницы и запуск авторизации
    mp = MainPage(driver)
    mp.authorization()
    mp.click_products_button()

    # Создаем объект страницы продукта и добавляем товар в корзину
    pp = ProductPage(driver)
    pp.select_and_add_to_cart()

    # Получаем цену с страницы продукта
    total_price_product_page = pp.get_total_price()

    # Создаем объект страницы чекаута
    cp = CheckoutPage(driver)

    # Получаем цену с страницы чекаута
    total_price_checkout_page = cp.get_cart_total_price()

    # Сравниваем цены с обеих страниц
    cp.assertion_prices_product_and_checkout_pages(total_price_product_page, total_price_checkout_page)
    cp.checkout_page_actions()

def test_buying_several_products(driver):
    print("Start Test")

    # Создание объекта страницы и запуск авторизации
    lp = MainPage(driver)
    lp.authorization_second()
    lp.click_products_button()

    pp = ProductPage(driver)
    pp.select_products_from_all_tabs()

    cp = CheckoutPage(driver)
    cp.click_cart_proceed_button()
    cp.assert_checkout_page_product_names()
    cp.click_get_button_next_to_payment()



