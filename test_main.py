import pytest

from textbox_page import TextBoxPage
from base_page import BasePage


file_path = '/Users/bebe/PycharmProjects/demoqa_po/datatabs.xlsx'
link = 'https://demoqa.com/text-box'


@pytest.mark.parametrize('data', BasePage.load_excel_data(file_path))
def test_fill_the_form(driver, data):
    page = TextBoxPage(driver, url=link)
    page.open()
    page.fill_the_name(data['Name'])
    page.fill_the_email(data['Email'])
    page.fill_the_cur_addr(data['Current Address'])
    page.fill_the_per_addr(data['Permananet Address'])
    page.press_submit()
    outputs = page.get_border_text()
    assert_values(outputs, data)
    pass


def assert_values(element_text, data):
    lines = element_text.split('\n')

    # Создайте словарь для хранения данных из элемента
    element_data = {}

    # Разделите каждую строку на ключ и значение
    for line in lines:
        parts = line.split(':')
        key = parts[0].strip()
        value = parts[1].strip()
        element_data[key] = value

    for key, value in data.items():
        if key in element_data and element_data[key] == value:
            print(f"\nЗначение для ключа '{key}' совпадает: {value}")
        else:
            print(f"\nЗначение для ключа '{key}' не совпадает: {value}")
    pass
