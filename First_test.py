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
password.send_keys("secret_sauce")
print("Input Password")

# Находим кнопку входа на странице с помощью XPath выражения
# XPath выражение ищет элемент input с атрибутом id="login-button"
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")

# Выполняем клик по найденной кнопке входа
# Метод click() имитирует нажатие левой кнопки мыши на элементе
button_login.click()
print("Click Login Button")

# Получаем текущий URL после входа и выводим его
print(driver.current_url)

# Сохраняем текущий URL в переменную для дальнейшей проверки
get_url = driver.current_url

# Ожидаемый URL после успешного входа
url = "https://www.saucedemo.com/inventory.html"

# Проверяем, что текущий URL соответствует ожидаемому
# Это подтверждает успешный вход в систему
assert url == get_url
print("URL корректен")  # Выводим сообщение об успешной проверке URL

# Находим элемент с заголовком "Products" на странице
text_products = driver.find_element(By.XPATH, "//span[@class='title']")

# Выводим текст найденного элемента заголовка
print(f"Заголовок: {text_products.text}")

# Сохраняем текст заголовка в переменную для проверки
value_text_products = text_products.text

# Проверяем, что текст заголовка соответствует ожидаемому значению "Products"
# Это подтверждает, что мы находимся на правильной странице после входа
assert value_text_products == "Products"
print("Заголовок корректен")  # Выводим сообщение об успешной проверке заголовка