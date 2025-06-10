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

# Находим кнопку для добавления в корзину с помощью XPath выражения и кликаем
button_add_backpack = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]').click()
button_add_bike = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]').click()
button_add_shirt = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
button_add_jacket = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
button_add_onesie = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-onesie"]').click()
button_add_shirt_red = driver.find_element(By.XPATH, '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
# Находим ссылку корзины с помощью XPath выражения и кликаем
button_shopping_cart = driver.find_element(By.XPATH, '//a[@data-test="shopping-cart-link"]').click()

#Создаем объект ActionsChains
actions = ActionChains(driver)
# Находим элемент по его идентификатору (ID) "item_3_title_link"
element = driver.find_element(By.ID, "item_3_title_link")
# Перемещаем курсор мыши к найденному элементу с помощью ActionChains
actions.move_to_element(element).perform()




#driver.execute_script("window/scrollTo(0, 1000);")