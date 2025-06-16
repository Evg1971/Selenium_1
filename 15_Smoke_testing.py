from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#Функция для входа в систему
def login(driver, username, password):
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()
# Функция для получения информации о продукте
def get_product_info(driver, product_xpath, price_xpath):
    product_name = driver.find_element(By.XPATH, product_xpath).text
    product_price = driver.find_element(By.XPATH, price_xpath).text
    print(f"Product: {product_name}, Price: {product_price}")
    return product_name, product_price

# Функция для заполнения формы оформления заказа
def fill_checkout_form(driver, first_name, last_name, postal_code):
    driver.find_element(By.XPATH, '//input[@id="first-name"]').send_keys(first_name)
    print("Input First Name")
    driver.find_element(By.XPATH, '//input[@id="last-name"]').send_keys(last_name)
    print("Input Last Name")
    driver.find_element(By.XPATH, '//input[@id="postal-code"]').send_keys(postal_code)
    print("Input Postal Code")
    driver.find_element(By.XPATH, '//input[@id="continue"]').click()
    print("Clicked Continue")

# Настройка опций Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Создание экземпляра драйвера
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# Основной URL
base_url = 'https://www.saucedemo.com/'

# Открытие страницы
driver.get(base_url)

# Вход в систему
login(driver, "standard_user", "secret_sauce")

# Получаем информацию о первом продукте и добавляем его в корзину
product_1_info = get_product_info(
    driver,
    '//*[@id="item_4_title_link"]',
    '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div'
)
product_1, price_product_1 = product_1_info
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
print('Select Product_1')

# Получаем информацию о втором продукте и добавляем его в корзину
product_2_info = get_product_info(
    driver,
    '//*[@id="item_0_title_link"]/div',
    '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div'
)
product_2, price_product_2 = product_2_info
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
print("Select Product 2")

# Переход в корзину и оформление заказа
driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
print("Click Cart")
driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
print("Click Checkout")

# Заполнение формы заказа
fill_checkout_form(driver, "Ivan", "Ivanov", "12345")

# Проверка информации о первом продукте в заказе
finish_product_1_info = get_product_info(
    driver,
    '//a[@id="item_4_title_link"]',
    '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div'
)
finish_product_1, price_finish_product_1 = finish_product_1_info
assert product_1 == finish_product_1
print("Info Finish Product 1 Good")
assert price_product_1 == price_finish_product_1
print("Info Price Finish Product 1 Good")

# Проверка информации о втором продукте в заказе
finish_product_2_info = get_product_info(
    driver,
    '//*[@id="item_0_title_link"]/div',
    '//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div'
)
finish_product_2, price_finish_product_2 = finish_product_2_info
assert product_2 == finish_product_2
print("Finish Product 2 Good")
assert price_product_2 == price_finish_product_2
print("Info Price Finish Product 2 Good")

# Проверка общей суммы заказа
summary_price_text = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]').text
print(summary_price_text)
price_1 = float(price_product_1.replace("$", ""))
price_2 = float(price_product_2.replace("$", ""))
item_total = "Item total: " + "$" + str(price_1 + price_2)
assert summary_price_text == item_total, "Summary price mismatch"
print("Summary Price Good")

# Завершение заказа
driver.find_element(By.XPATH, '//*[@id="finish"]').click()
print("Click Finish")
value_checkout_complete = driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/h2').text
print(value_checkout_complete)
assert value_checkout_complete == "Thank you for your order!", "Order completion message mismatch"
print("Info Order Complete Good")
