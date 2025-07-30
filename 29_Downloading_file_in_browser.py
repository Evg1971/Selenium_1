# Импорт необходимых библиотек
import glob  # Для поиска файлов по шаблону
import os  # Для работы с операционной системой и файлами
import time  # Для использования функций времени, таких как sleep

# Импорт библиотек для работы с Selenium
from selenium import webdriver  # Основной модуль Selenium для управления браузером
from selenium.webdriver.chrome.service import Service as ChromeService  # Для управления сервисом Chrome
from selenium.webdriver.common.by import By  # Для поиска элементов на странице
from webdriver_manager.chrome import ChromeDriverManager  # Для автоматического управления драйвером Chrome

# Указание пути для сохранения скачанных файлов
path_download = r"C:\Users\Катя\PycharmProjects\Selenium_1\files_download"

# Настройка опций Chrome
options = webdriver.ChromeOptions()  # Создание объекта опций для Chrome
prefs = {'download.default_directory': path_download}  # Установка директории для скачивания по умолчанию
options.add_experimental_option('prefs', prefs)  # Добавление настроек в опции Chrome
options.add_experimental_option("detach", True)  # Предотвращает автоматическое закрытие браузера после завершения скрипта

# Создание экземпляра драйвера Chrome с заданными опциями и сервисом
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())  # Автоматическая установка и настройка драйвера Chrome
)

# Основной URL сайта для скачивания файлов
base_url = 'https://the-internet.herokuapp.com/download'

# Открытие страницы по указанному URL
driver.get(base_url)

# Ожидание загрузки страницы (3 секунды)
time.sleep(3)

# Поиск и нажатие кнопки скачивания файла
click_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/a[5]')  # Поиск элемента по XPath
click_button.click()  # Нажатие на кнопку скачивания
print("The download button is pressed")  # Вывод сообщения о нажатии кнопки

# Ожидание завершения скачивания файла (5 секунд)
time.sleep(5)

# Указание имени файла для проверки
file_name = "Newt.txt"

# Формирование полного пути к файлу
file_path = os.path.join(path_download, file_name)

# Вывод пути к скачанному файлу
print(f"The path of the downloaded file: {file_path}")

# Проверка существования файла по указанному пути
assert os.access(file_path, os.F_OK) == True, "The file is missing in the directory"
print("File in directory")  # Вывод сообщения о наличии файла в директории

# Поиск всех файлов в директории скачивания
files = glob.glob(os.path.join(path_download, "*.*"))

# Проверка размера каждого найденного файла
for file in files:
    # Получение размера файла в байтах
    file_size = os.path.getsize(file)

    # Проверка, что файл не пустой (размер больше 100 байт)
    if file_size > 100:
        print(f"The file {file_name} is not empty (size: {file_size} bytes)")
    else:
        print(f"The file {file_name} is empty")

# Завершение работы браузера и вывод сообщения об этом
driver.quit()
print("The Chrome browser is closed")