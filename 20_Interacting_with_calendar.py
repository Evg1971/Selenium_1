import time

from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#Настройка опций Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Эта опция предотвращает автоматическое закрытие браузера после завершения скрипта

#Создание экземпляра драйвера
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

#Основной URL
base_url = 'https://practice-automation.com/calendars/#contact-form-1065-2-1'
#Открытие страницы
driver.get(base_url)
#Установка размера окна
driver.set_window_size(1920, 1080)

#Находим поле для ввода даты по XPATH
date_input = driver.find_element(By.XPATH, '//input[@id="g1065-2-1-selectorenteradate"]')

#Получаем текущую дату и добавляем к ней 10 дней
new_date = (datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d")

#Вводим новую дату в элемент
date_input.send_keys(new_date)

#Выводим информацию на экран о действии
print("Date entered plus 10 days:", new_date)

time.sleep(3)

#Завершение работы браузера
driver.quit()
print("The Chrome browser is closed")