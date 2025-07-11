# Импорт модуля time для использования функций, связанных со временем, таких как sleep
import time

# Импорт модуля webdriver из selenium для управления браузером
from selenium import webdriver
# Импорт класса Service из модуля selenium.webdriver.chrome.service для управления сервисом ChromeDriver
from selenium.webdriver.chrome.service import Service as ChromeService
# Импорт класса By из модуля selenium.webdriver.common.by для поиска элементов на странице
from selenium.webdriver.common.by import By
# Импорт класса ChromeDriverManager из модуля webdriver_manager.chrome для управления драйвером Chrome
from webdriver_manager.chrome import ChromeDriverManager

# Настройка опций Chrome
options = webdriver.ChromeOptions()
# Добавление экспериментальной опции для предотвращения автоматического закрытия браузера после завершения скрипта
options.add_experimental_option("detach", True)

# Создание экземпляра драйвера Chrome с указанными опциями и сервисом
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# Основной URL для тестирования
base_url = 'https://lambdatest.com/selenium-playground/simple-form-demo'

# Открытие страницы в браузере
driver.get(base_url)

# Вывод сообщения о начале работы с блоком двух полей ввода
print("Block Two Input Fields")

# Задание значений для полей ввода
first_value = 123
second_value = 134
# Вычисление суммы значений
sum_result = first_value + second_value

# Поиск первого поля ввода по XPath и ввод значения
input_first_value = driver.find_element(By.XPATH, '//input[@id="sum1"]')
input_first_value.send_keys(first_value)
print("Enter First Value")

# Поиск второго поля ввода по XPath и ввод значения
input_second_value = driver.find_element(By.XPATH, '//input[@id="sum2"]')
input_second_value.send_keys(second_value)
print("Enter Second Value")

# Поиск кнопки "Get Sum" по XPath и клик по ней
click_button = driver.find_element(By.XPATH, '//*[@id="gettotal"]/button')
click_button.click()
print("Click Button 'Get Sum'")

time.sleep(2)# Пауза в 2 секунды для ожидания результата

# Поиск элемента с результатом по XPath и получение текста
result = driver.find_element(By.XPATH, '//p[@id="addmessage"]').text
# Проверка корректности суммы
assert str(sum_result) == result, "Summa Incorrect"
print("Summa Correct")

# Вывод сообщения о начале работы с блоком одного поля ввода
print("Block Single Input Field")

# Поиск поля ввода сообщения по XPath и ввод текста
input_message = driver.find_element(By.XPATH, '//input[@id="user-message"]')
message = "Hello, World!"
input_message.send_keys(message)
print("Write a message")

# Поиск кнопки отправки сообщения по XPath и клик по ней
click_button = driver.find_element(By.XPATH, '//button[@id="showInput"]')
click_button.click()
print("Send message")

time.sleep(2)

# Поиск элемента с сообщением по XPath и получение текста
your_message = driver.find_element(By.XPATH, '//p[@id="message"]')
value_message = your_message.text
# Проверка корректности сообщения
assert value_message == message, "The values are incorrect"
print("The values are correct")

time.sleep(2)# Пауза в 2 секунды перед закрытием браузера

# Завершение работы браузера
driver.quit()
print("The Chrome browser is closed")