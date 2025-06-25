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
# Добавляем задержку в 1 секунду для ожидания загрузки элементов
time.sleep(1)
# Находим и кликаем по чек-боксу 'Desktop'
driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[1]/span/label/span[1]').click()
print("Check Box Desktop is marked")
time.sleep(1)
# Находим и кликаем по чек-боксу 'Documents'
driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/span/label/span[1]').click()
print("Check Box Documents is marked")
time.sleep(1)
# Находим и кликаем по чек-боксу 'Downloads'
driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/span/label/span[1]').click()
print("Check Box Downloads is marked")
# Находим чекбокс "Home" и проверяем, что он выбран
check_box_home = driver.find_element(By.XPATH, '//input[@id="tree-node-home"]')
assert check_box_home.is_selected(), "Check Box Home is not selected!"
print("Check Box Home is selected")