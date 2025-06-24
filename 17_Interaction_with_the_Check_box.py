import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Настройка опций Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Эта опция предотвращает
# автоматическое закрытие браузера после завершения скрипта

# Создание экземпляра драйвера
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)
# Основной URL
base_url = ' https://demoqa.com/checkbox'
# Открытие страницы
driver.get(base_url)
# Установка размера окна
driver.set_window_size(1920, 1080)

# Находим и кликаем по стрелке для раскрытия меню
driver.find_element(By.XPATH, '//button[@aria-label="Toggle"]').click()
print("Menu Home open")  # Выводим сообщение о том, что меню открыто
# Добавляем задержку в 2 секунды для ожидания загрузки элементов
time.sleep(2)

# Находим чекбокс "Downloads", кликаем по нему и проверяем, что он выбран
check_box_downloads = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/span/label/span[1]')
check_box_downloads.click()  # Кликаем по чекбоксу
check_box_downloads.is_selected()  # Проверяем, что чекбокс выбран
print("Check Box Downloads is selected")  # Выводим сообщение о выборе чекбокса
# Добавляем задержку в 2 секунды
time.sleep(2)

# Находим чекбокс "Documents", кликаем по нему и проверяем, что он выбран
check_box_documents = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/span/label/span[1]')
check_box_documents.click()
check_box_documents.is_selected()
print("Check Box Documents is selected")
# Добавляем задержку в 2 секунды
time.sleep(2)

# Находим чекбокс "Desktop", кликаем по нему и проверяем, что он выбран
check_box_desktop = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[1]/span/label/span[1]')
check_box_desktop.click()
check_box_desktop.is_selected()
print("Check Box Desktop is selected")