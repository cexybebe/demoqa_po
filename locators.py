from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME = (By.ID, 'userName')
    EMAIL = (By.ID, 'userEmail')
    CUR_ADDRESS = (By.ID, 'currentAddress')
    PER_ADDRESS = (By.ID, 'permanentAddress')
    SUBMIT_BTN = (By.ID, 'submit')
    BORDER = (By.CLASS_NAME, 'border')
