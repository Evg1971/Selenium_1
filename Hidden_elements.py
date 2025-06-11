import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

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

# Находим поле ввода имени пользователя с помощью XPath выражения (кастомный метод)
user_name = driver.find_element(By.XPATH, "//input[@placeholder='Username']")

# Вводим текст "standard_user" в найденное поле ввода имени пользователя.
user_name.send_keys("standard_user")

# Находим поле ввода пароля с помощью XPath выражения(кастомный метод)
password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")

# Вводим текст "secret_sauce" в найденное поле ввода пароля.
password.send_keys("secret_sauce")

# Находим кнопку входа на странице с помощью XPath выражения
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")

# Выполняем клик по найденной кнопке входа
button_login.click()

#Нахождение элемента кнопки меню по XPath и сохранение его в переменной 'menu'
menu = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
#Клик по кнопке меню, чтобы открыть боковое меню
menu.click()
#Ожидание 1 секунды, чтобы убедиться, что меню успело открыться
time.sleep(1)
#Нахождение кнопки выхода из аккаунта по XPath и сохранение в переменной 'logout_button'
logout_button = driver.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]')
#Клик по кнопке выхода для завершения сеанса
logout_button.click()