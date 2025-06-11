import time

from selenium.webdriver.common.keys import Keys
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

# Вводим имя пользователя "standard_user"
user_name.send_keys("standard_user")
print("Input Login")  # Выводим сообщение о вводе логина

# Находим поле ввода пароля с помощью XPath по атрибуту id
password = driver.find_element(By.XPATH, "//input[@id='password']")

# Вводим корректный пароль "secret_sauce"
password.send_keys("secret_sauce")
print("Input Password")  # Выводим сообщение о вводе пароля
time.sleep(2)

# Выделяем весь текст в поле ввода имени пользователя
user_name.send_keys(Keys.CONTROL + 'a')
time.sleep(2)  # Делаем паузу в 2 секунды
# Удаляем выделенный текст из поля ввода имени пользователя
user_name.send_keys(Keys.BACKSPACE)
time.sleep(2)   # Делаем паузу в 2 секунды
# Выделяем весь текст в поле ввода пароля
password.send_keys(Keys.CONTROL + 'a')
time.sleep(2)   # Делаем паузу в 2 секунды
# Удаляем выделенный текст из поля ввода пароля
password.send_keys(Keys.BACKSPACE)
time.sleep(2)   # Делаем паузу в 2 секунды
# Находим кнопку входа на странице с помощью XPath
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")

button_login.click() # Выполняем клик по найденной кнопке входа

# Выводим сообщение о нажатии кнопки входа
print("Click Login Button")
