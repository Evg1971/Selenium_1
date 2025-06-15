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

# Находим первый продукт по XPath и получаем его название
product_1 = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]')
value_product_1 = product_1.text
print(value_product_1)
# Находим цену первого продукта по XPath и выводим её
price_product_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
value_price_product_1 = price_product_1.text
print(value_price_product_1)
# Находим кнопку добавления первого продукта в корзину и кликаем по ней
select_product_1 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
select_product_1.click()
print('Select Product_1')
# Находим второй продукт по XPath и получаем его название
product_2 = driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div')
value_product_2 = product_2.text
print(value_product_2)
# Находим цену второго продукта по XPath и выводим её
price_product_2 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')
value_price_product_2 = price_product_2.text
print(value_price_product_2)
# Находим кнопку добавления второго продукта в корзину и кликаем по ней
select_product_2 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
select_product_2.click()
print("Select Product 2")
# Находим иконку корзины и кликаем по ней
cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
cart.click()
print("Click Cart")
# Находим кнопку оформления заказа и кликаем по ней
checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
checkout.click()
print("Click Checkout")
# Находим поле для ввода имени и вводим значение "Ivan"
first_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
first_name.send_keys("Ivan")
print("Input First Name")
# Находим поле для ввода фамилии и вводим значение "Ivanov"
last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
last_name.send_keys("Ivanov")
print("Input Last Name")
# Находим поле для ввода почтового индекса и вводим значение "12345"
postal_code = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
postal_code.send_keys("12345")
print("Input Postal Code")
# Находим кнопку продолжения и кликаем по ней
button_continue = driver.find_element(By.XPATH, '//input[@id="continue"]')
button_continue.click()
print("Click Button Continue")
# Находим название первого продукта на странице оформления заказа и проверяем его соответствие
finish_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print("Finish Product 1 Good")
# Находим цену первого продукта на странице оформления заказа и проверяем её соответствие
price_finish_product_1 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_price_finish_product_1 = price_finish_product_1.text
print(value_price_finish_product_1)
assert value_price_product_1 == value_price_finish_product_1
print("Info Price Finish Product 1 Good")
# Находим название второго продукта на странице оформления заказа и проверяем его соответствие
finish_product_2 = driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div')
value_finish_product_2 = finish_product_2.text
print(value_finish_product_2)
assert value_product_2 == value_finish_product_2
print("Finish Product 2 Good")
# Находим цену второго продукта на странице оформления заказа и проверяем её соответствие
price_finish_product_2 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_price_finish_product_2 = price_finish_product_2.text
print(value_price_finish_product_2)
assert value_price_product_2 == value_price_finish_product_2
print("Info Price Finish Product 2 Good")
# Находим общую сумму заказа и проверяем её соответствие сумме цен продуктов
summary_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
value_summary_price = summary_price.text
print(value_summary_price)
price_1 = float(value_price_product_1.replace("$", ""))
price_2 = float(value_price_product_2.replace("$", ""))
item_total = "Item total: " + "$" + str(price_1 + price_2)
assert value_summary_price == item_total
print("Summary Price Good")
# Находим кнопку завершения заказа и кликаем по ней
button_finish = driver.find_element(By.XPATH, '//*[@id="finish"]')
button_finish.click()
print("Click Finish")
# Находим сообщение о завершении заказа и проверяем его соответствие ожидаемому тексту
checkout_complete = driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/h2')
value_checkout_complete = checkout_complete.text
print(value_checkout_complete)
assert value_checkout_complete == "Thank you for your order!"
print("Info Order Complete Good")