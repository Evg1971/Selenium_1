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
base_url = 'https://saucedemo.com/'

# Открытие страницы
driver.get(base_url)

# Установка размера окна
driver.set_window_size(1920, 1080)

# Находим поле ввода имени пользователя с помощью XPath по атрибуту id
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")

# Вводим неверное имя пользователя "standart_us" (с ошибкой в написании)
user_name.send_keys("standart_us")
print("Input Login")  # Выводим сообщение о вводе логина

# Находим поле ввода пароля с помощью XPath по атрибуту id
password = driver.find_element(By.XPATH, "//input[@id='password']")

# Вводим корректный пароль "secret_sauce"
password.send_keys("secret_sauce")
print("Input Password")  # Выводим сообщение о вводе пароля

# Находим кнопку входа с помощью XPath по атрибуту id
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")

# Нажимаем кнопку входа для отправки формы
button_login.click()
print("Click Login Button")  # Выводим сообщение о нажатии кнопки входа

# Делаем паузу в 3 секунды
time.sleep(3)

# Обновляем текущую страницу
driver.refresh()
