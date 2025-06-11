from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Настройка опций Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Эта опция предотвращает
# автоматическое закрытие браузера после завершения скрипта

# Добавляем аргумент для запуска браузера в headless режиме
options.add_argument("--headless")

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
# XPATH ищет элемент input с атрибутом placeholder="Username"
user_name = driver.find_element(By.XPATH, "//input[@placeholder='Username']")

# Вводим текст "standard_user" в найденное поле ввода имени пользователя.
user_name.send_keys("standard_user")
print("Input Login")

# Находим поле ввода пароля с помощью XPath выражения(кастомный метод)
# XPath ищет любой элемент input с атрибутом placeholder="Password"
password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")

# Вводим текст "secret_sauce" в найденное поле ввода пароля.
password.send_keys("secret")
print("Input Password")

# Находим кнопку входа на странице с помощью XPath выражения
# XPath выражение ищет элемент input с атрибутом id="login-button"
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")

# Выполняем клик по найденной кнопке входа
# Метод click() имитирует нажатие левой кнопки мыши на элементе
button_login.click()
print("Click Login Button")

# Находим элемент с сообщением об ошибке на странице
# XPath выражение ищет элемент h3 с атрибутом data-test="error"
# Этот элемент появляется при неудачной попытке входа # и содержит сообщение об ошибке
warning_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")

# Получаем текстовое содержимое найденного элемента с сообщением об ошибке в фомате text
value_warning_text = warning_text.text

# Проверяем, что текст сообщения об ошибке соответствует ожидаемому значению
assert value_warning_text == "Epic sadface: Username and password do not match any user in this service"

# Выводим сообщение об успешной проверке текста ошибки
# (система корректно обрабатывает неверные учетные данные)
print("Сообщение корректно")

# Находим кнопку закрытия сообщения об ошибке на странице
error_button = driver.find_element(By.XPATH, "//button[@class='error-button']")
# Выполняем клик по найденной кнопке закрытия сообщения об ошибке
error_button.click()
# Выводим сообщение о нажатии кнопки закрытия ошибки
print("Click Error Button")