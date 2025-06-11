import time

from selenium import webdriver
from selenium.webdriver import Keys
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

print("Input Login")

# Находим поле ввода пароля с помощью XPath выражения(кастомный метод)
password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")

# Вводим текст "secret_sauce" в найденное поле ввода пароля.
password.send_keys("secret_sauce")
print("Input Password")

time.sleep(3) # пауза 3с

# Выделяем весь текст в поле user_name
user_name.send_keys(Keys.CONTROL + 'a')
# Удаляем выделенный текст, очищая поле
user_name.send_keys(Keys.DELETE)
# Выделяем весь текст в поле password
password.send_keys(Keys.CONTROL + 'a')
# Удаляем выделенный текст, очищая поле
password.send_keys(Keys.DELETE)

time.sleep(3) # пауза 3с

# Вводим текст "standard_user" в найденное поле ввода имени пользователя.
user_name.send_keys("standard_user")
print("Input Login")

# Вводим текст "secret_sauce" в найденное поле ввода пароля.
password.send_keys("secret_sauce")
print("Input Password")

time.sleep(3) # пауза 3с
# Находим кнопку входа на странице с помощью XPath выражения
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
# Выполняем клик по найденной кнопке входа
button_login.click()
print("Input Login Button")
