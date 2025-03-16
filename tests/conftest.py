import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    # Настройки браузера
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")  # Открытие в режиме инкогнито
    options.add_experimental_option("detach", True)

    # Запуск WebDriver
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    yield driver  # Передача драйвера в тест

    # Закрытие браузера после теста
    print("End test")

