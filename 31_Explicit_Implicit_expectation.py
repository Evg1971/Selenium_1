import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

# Инициализация генератора тестовых данных
fake = Faker()

def print_product_info():
    print("Приветствую тебя в нашем интернет-магазине")
    print("Выбери один из следующих товаров и укажи его номер:\n"
          "1 - Sauce Labs Backpack\n"
          "2 - Sauce Labs Bike Light\n"
          "3 - Sauce Labs Bolt T-Shirt\n"
          "4 - Sauce Labs Fleece Jacket\n"
          "5 - Sauce Labs Onesie\n"
          "6 - Test.allTheThings() T-Shirt (Red)")


def get_product_selector(product_number):
    product_selector = {
        1: '//button[@id="add-to-cart-sauce-labs-backpack"]',
        2: '//button[@id="add-to-cart-sauce-labs-bike-light"]',
        3: '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]',
        4: '//button[@id="add-to-cart-sauce-labs-fleece-jacket"]',
        5: '//button[@id="add-to-cart-sauce-labs-onesie"]',
        6: '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]'
    }
    return product_selector.get(product_number, "")


def get_product_name(product_number):
    product_names = {
        1: "Sauce Labs Backpack",
        2: "Sauce Labs Bike Light",
        3: "Sauce Labs Bolt T-Shirt",
        4: "Sauce Labs Fleece Jacket",
        5: "Sauce Labs Onesie",
        6: "Test.allTheThings() T-Shirt (Red)"
    }
    return product_names.get(product_number, "")


def get_product_price(product_number):
    product_price = {
        1: "$29.99",
        2: "$9.99",
        3: "$15.99",
        4: "$49.99",
        5: "$7.99",
        6: "$15.99"
    }
    return product_price.get(product_number)

# Настройка опций Chrome
options = webdriver.ChromeOptions()  # Создание объекта опций для настройки параметров браузера Chrome

# Добавление экспериментальной опции для предотвращения автоматического закрытия браузера после завершения скрипта
options.add_experimental_option("detach", True)

# Создание экземпляра драйвера Chrome с указанными опциями и сервисом
# ChromeDriverManager автоматически скачивает и настраивает нужную версию драйвера Chrome
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# Установка неявного ожидания (implicit wait) - 10 секунд
# Это ожидание будет применяться ко всем поискам элементов
driver.implicitly_wait(10)

# Основной URL для тестирования
base_url = 'https://www.saucedemo.com/'

# Открытие страницы в браузере по указанному URL
driver.get(base_url)
print("Открыта главная страница сайта")

time.sleep(2)

# Вход в систему
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
username.send_keys("standard_user")
password.send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
print("Успешный вход в систему")

time.sleep(2)

# Вывод информации о товарах для пользователя
print_product_info()

# Получение выбора пользователя
while 1:
    try:
        product_number = int(input("Введите номер товара (1-6): "))
        if 1 <= product_number <= 6:
            break
        print("Пожалуйста, введите число от 1 до 6")
    except ValueError:
        print("Пожалуйста, введите корректное число")


# Получение информации о выбранном товаре
product_name = get_product_name(product_number)
product_price = get_product_price(product_number)
product_selector = get_product_selector(product_number)
print(f"Вы выбрали: {product_name}, цена: {product_price}")

# Добавление товара в корзину
driver.find_element(By.XPATH, product_selector).click()
print(f"Товар {product_name} добавлен в корзину")

time.sleep(2)

# Переход в корзину
driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
print("Переход в корзину")

# Проверка информации о товаре в корзине
cart_item_name = driver.find_element(By.CLASS_NAME, 'inventory_item_name').text
cart_item_price = driver.find_element(By.CLASS_NAME, 'inventory_item_price').text
print(f"В корзине: {cart_item_name}, цена: {cart_item_price}")

# Проверка соответствия информации
assert product_name == cart_item_name, f"Название товара не совпадает. Ожидалось: {product_name}, получено: {cart_item_name}"
assert product_price == cart_item_price, f"Цена товара не совпадает. Ожидалось: {product_price}, получено: {cart_item_price}"
print("Информация о товаре в корзине совпадает с выбранным товаром")

time.sleep(2)

# Переход к оформлению заказа
driver.find_element(By.XPATH, '//button[@id="checkout"]').click()
print("Переход к оформлению заказа")

time.sleep(2)

# Заполнение информации о покупателе с использованием сгенерированных данных
first_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
postal_code = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
continue_button = driver.find_element(By.XPATH, '//input[@id="continue"]')

# Генерация тестовых данных с помощью Faker
first_name.send_keys(fake.first_name())
last_name.send_keys(fake.last_name())
postal_code.send_keys(fake.zipcode())
print("Данные покупателя заполнены сгенерированными значениями")

time.sleep(2)

continue_button.click()
print("Переход к завершению оформления заказа")

time.sleep(2)

# Завершение оформления заказа
driver.find_element(By.XPATH, '//button[@id="finish"]').click()
print("Заказ оформлен")

# Проверка успешного оформления заказа
try:
    success_message = driver.find_element(By.XPATH, '//h2[@class="complete-header"]').text
    print(f"Заказ успешно оформлен: {success_message}")
    assert success_message == "Thank you for your order!", "Сообщение об успешном оформлении заказа не совпадает"
except NoSuchElementException:
    print("Не удалось подтвердить успешное оформление заказа")
    raise AssertionError("Не удалось найти подтверждение оформления заказа")

time.sleep(2)

# Закрытие браузера
driver.quit()
print("Браузер закрыт")
