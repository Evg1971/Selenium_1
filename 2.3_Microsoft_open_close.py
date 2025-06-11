import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Создание экземпляра драйвера для Microsoft Edge
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

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
