from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time


class BasePage:
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_url_correct(self, substring):
        url = str(self.driver.current_url)
        return substring in url

    @staticmethod
    def load_excel_data(file_path):
        # Загрузка данных из Excel файла
        df = pd.read_excel(file_path)

        # Извлечение ключей из первой строки
        keys = df.iloc[0].tolist()

        # Извлечение значений из остальных строк
        values = df.iloc[1:].values.tolist()

        # Создание списка кортежей с парами ключ-значение
        data = [dict(zip(keys, row)) for row in values]

        return data
