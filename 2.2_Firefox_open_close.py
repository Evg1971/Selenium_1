import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Создание экземпляра драйвера
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Основной URL
base_url = 'https://saucedemo.com/'

# Открытие страницы
driver.get(base_url)

# Установка размера окна
driver.set_window_size(1920, 1080)
# Время, в течение которого сайт будет открыт
time.sleep(5)
# Закрытие текущего окна браузера
driver.close()