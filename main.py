from selenium import webdriver

# Создайте экземпляр драйвера Chrome
driver = webdriver.Chrome()

# Получите журнал сообщений
log_entries = driver.get_log('driver')

# Просмотрите журнал, чтобы узнать, откуда загружен ChromeDriver
for entry in log_entries:
    print(entry)