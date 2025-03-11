class Base:
    """ Базовый класс, содержащий универсальные методы """
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Метод проверки url"""
        get_url = self.driver.current_url
        print("current url " + get_url)

    def assert_url(self, result):
        """Проверка корректности URL"""
        get_url = self.driver.current_url
        print(get_url)
        assert result == get_url
        print("--Корректная URL--")

    def assert_word_sign_in(self, word, result):
        """Проверка значения текста"""
        value_word = word.text
        assert value_word == result
        print(f"Текст {value_word} совпадает с {result}")
