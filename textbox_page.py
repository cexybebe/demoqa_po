import time

from locators import TextBoxPageLocators
from base_page import BasePage


class TextBoxPage(BasePage):
    def fill_the_name(self, text):
        self.driver.find_element(*TextBoxPageLocators.FULL_NAME).send_keys(text)
        pass

    def fill_the_email(self, text):
        self.driver.find_element(*TextBoxPageLocators.EMAIL).send_keys(text)
        pass

    def fill_the_cur_addr(self, text):
        self.driver.find_element(*TextBoxPageLocators.CUR_ADDRESS).send_keys(text)
        pass

    def fill_the_per_addr(self, text):
        self.driver.find_element(*TextBoxPageLocators.PER_ADDRESS).send_keys(text)
        pass

    def press_submit(self):
        btn = self.driver.find_element(*TextBoxPageLocators.SUBMIT_BTN)

        # Прокручиваем страницу на 100 пикселей вниз
        self.driver.execute_script("window.scrollBy(0, 200);")

        # Теперь элемент должен быть кликабельным, вы можете выполнить клик по нему
        btn.click()
        pass

    def get_border_text(self):
        ans = self.driver.find_element(*TextBoxPageLocators.BORDER).text
        return ans
        pass
    pass
