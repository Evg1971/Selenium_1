# Импорт необходимых библиотек
import time  # Для использования функций времени, таких как sleep

# Импорт библиотек для работы с Selenium и Faker
from faker import Faker  # Для генерации фейковых данных
from selenium import webdriver  # Основной модуль Selenium для управления браузером
from selenium.webdriver.chrome.service import Service as ChromeService  # Для управления сервисом Chrome
from selenium.webdriver.common.by import By  # Для поиска элементов на странице
from webdriver_manager.chrome import ChromeDriverManager  # Для автоматического управления драйвером Chrome

# Настройка опций Chrome
options = webdriver.ChromeOptions()  # Создание объекта опций для Chrome
options.add_experimental_option("detach", True)  # Эта опция предотвращает автоматическое закрытие браузера после завершения скрипта

# Создание экземпляра драйвера Chrome с заданными опциями и сервисом
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())  # Автоматическая установка и настройка драйвера Chrome
)

# Основной URL сайта, который будет открыт
base_url = 'https://saucedemo.com/'

# Открытие страницы по указанному URL
driver.get(base_url)

# Пауза на 2 секунды для загрузки страницы
time.sleep(2)

# Создание экземпляра Faker для генерации фейковых данных на английском языке
fake = Faker("en_US")

# Генерация фейкового имени
name = fake.first_name()

# Поиск элемента поля ввода логина по XPath
user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')

# Ввод сгенерированного имени в поле логина
user_name.send_keys(name)

# Вывод сообщения в консоль о вводе логина
print("Input Login")

# Пауза на 2 секунды
time.sleep(2)

# Завершение работы браузера
driver.quit()

# Вывод сообщения в консоль о закрытии браузера
print("The Chrome browser is closed")