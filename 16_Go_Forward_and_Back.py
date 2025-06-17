import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Функция для входа в систему
def login(driver, username, password):
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)
    print("Input Login")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
    print("Input Password")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()
    print("Authorization Good")


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
# Добавление товара в корзину
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
print('Select Product_1')
# Переход в корзину
driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
print("Click Cart")
time.sleep(2) # Пауза 2с
# Возврат назад на предыдущую страницу
driver.back()
print("Go Back")
time.sleep(2) # Пауза 2с
# Переход вперед на следующую страницу обратно
driver.forward()
print("Go Forward")