# Импорт необходимых библиотек
import time  # Для использования функций времени, таких как sleep

# Импорт библиотек для работы с Selenium
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

# Основной URL сайта для загрузки файлов
base_url = 'https://www.lambdatest.com/selenium-playground/upload-file-demo'

# Открытие страницы по указанному URL
driver.get(base_url)

# Путь к файлу, который будет загружен
path_upload = r"C:\Users\Катя\PycharmProjects\Selenium_1\Screen\Swag_Labs_2025.06.09-15.00.17.png"

# Поиск элемента для загрузки файла по XPath
click_button = driver.find_element(By.XPATH, '//input[@class="w-full"]')

# Загрузка файла через отправку пути к файлу в элемент input
click_button.send_keys(path_upload)
print("The file is uploaded")  # Сообщение об успешной загрузке

# Получение имени файла из атрибута value и извлечение только имени файла
filename = click_button.get_attribute("value").split("\\")[-1]

# Ожидаемое имя файла для сравнения
name_file = "Swag_Labs_2025.06.09-15.00.17.png"

# Проверка соответствия имен файлов
assert filename == name_file, "The file names don't match"
print("Success: File names match")  # Сообщение об успешном совпадении имен

# Пауза в 2 секунды перед закрытием браузера
time.sleep(2)

# Завершение работы браузера и вывод сообщения об этом
driver.quit()
print("The Chrome browser is closed")