# Импорт модуля time для использования функций задержки
# Необходим для создания пауз между действиями в тесте
import time

# Импорт основного класса webdriver для управления браузером
# Основной класс для автоматизации браузера в Selenium
from selenium import webdriver

# Импорт класса Service для настройки сервиса ChromeDriver
# Позволяет управлять сервисом драйвера Chrome
from selenium.webdriver.chrome.service import Service as ChromeService

# Импорт класса By для поиска элементов по различным локаторам
# Содержит константы для поиска элементов (ID, XPATH, CSS_SELECTOR и др.)
from selenium.webdriver.common.by import By

# Импорт менеджера драйверов для автоматической установки ChromeDriver
# Автоматически скачивает и устанавливает нужную версию драйвера Chrome
from webdriver_manager.chrome import ChromeDriverManager

# Импорт конкретных исключений для обработки ошибок
# NoSuchElementException - элемент не найден на странице
# WebDriverException - общие ошибки WebDriver
# TimeoutException - элемент не появился за указанное время
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException

class Test:
    """Класс для тестирования сайта"""

    def __init__(self):
        """Конструктор класса."""
        # Настройка опций Chrome
        self.options = webdriver.ChromeOptions()

        # Опция предотвращает автоматическое закрытие браузера после завершения скрипта
        # Это позволяет визуально проверять результаты выполнения тестов
        self.options.add_experimental_option("detach", True)

        # Создание экземпляра драйвера Chrome с указанными опциями
        # ChromeDriverManager автоматически скачивает и устанавливает нужную версию драйвера
        self.driver = webdriver.Chrome(
            options=self.options,
            service=ChromeService(ChromeDriverManager().install())
        )

    def open_page(self, url, width, height):
        """Метод для открытия веб-страницы."""
        # Открытие страницы в браузере по указанному URL
        self.driver.get(url)

        # Установка размера окна браузера
        self.driver.set_window_size(width, height)

        # Вывод сообщения об успешном открытии страницы
        print(f"Страница {url} успешно открыта с разрешением {width}x{height}")

    def login(self, username, password):
        """Метод для авторизации на сайте."""
        try:
            # Поиск поля ввод имени пользователя
            self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)

            # Поиск поля и ввод пароля
            self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)

            # Поиск кнопки входа по XPath и клик по ней
            self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()

            # Вывод сообщения об успешной авторизации
            print("Авторизация прошла успешно")

        except NoSuchElementException as e:
            # Обработка случая, когда элемент не найден на странице
            print(f"Элемент не найден на странице: {str(e)}")
            raise

        except WebDriverException as e:
            # Обработка общих ошибок WebDriver
            print(f"Ошибка при авторизации: {str(e)}")
            raise

    def close(self):
        """Метод для закрытия браузера."""
        try:
            # Метод quit() закрывает все окна браузера и завершает сеанс WebDriver
            self.driver.quit()
            print("Браузер успешно закрыт")

        except WebDriverException as e:
            # Обработка ошибок при закрытии браузера
            print(f"Ошибка при закрытии браузера: {str(e)}")
            raise

# Создание экземпляра тестового класса
start_test = Test()

try:
    # Открытие главной страницы сайта SauceDemo
    # Указываем URL и размер окна браузера (ширина, высота)
    start_test.open_page("https://www.saucedemo.com/", 1920, 1020)

    # Пауза в 2 секунды для визуальной проверки открытия страницы
    time.sleep(2)

    # Авторизация на сайте с использованием стандартных учетных данных
    # Передаем имя пользователя и пароль
    start_test.login("standard_user", "secret_sauce")

    # Пауза в 3 секунды для визуальной проверки успешной авторизации
    time.sleep(3)

except NoSuchElementException as e:
    # Обработка ошибки, когда элемент не найден на странице
    print(f"Элемент не найден: {str(e)}")

except WebDriverException as e:
    # Обработка общих ошибок WebDriver
    print(f"Ошибка WebDriver: {str(e)}")

except TimeoutException as e:
    # Обработка ошибок таймаута
    print(f"Таймаут ожидания элемента: {str(e)}")

finally:
    # Закрытие браузера в блоке finally для гарантированного выполнения
    # Выполняется независимо от того, завершился тест успешно или с ошибкой
    start_test.close()