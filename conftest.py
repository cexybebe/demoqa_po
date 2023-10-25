import pytest
from selenium import webdriver


@pytest.fixture
def lang(request):
    return request.config.getoption("--language", default="ru")


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: en, es, fr, etc.")


@pytest.fixture(scope="function")
def driver(request):
    print("\nstartинг browser for test..")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--window-size={1920},{1080}')

    driver = webdriver.Chrome(chrome_options=chrome_options)

    yield driver
    print("\nquitинг browser..")
    driver.quit()
