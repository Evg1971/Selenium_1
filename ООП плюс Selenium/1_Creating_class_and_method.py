# Импорт модуля time для использования функций задержки
import time
# Импорт основного класса webdriver для управления браузером
from selenium import webdriver
# Импорт класса Service для настройки сервиса ChromeDriver
from selenium.webdriver.chrome.service import Service as ChromeService
# Импорт класса By для поиска элементов по различным локаторам
from selenium.webdriver.common.by import By
# Импорт менеджера драйверов для автоматической установки ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager

class TestSauceDemo:
    """Класс для тестирования сайта SauceDemo."""

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

    def open_page(self):
        """Метод для открытия главной страницы сайта SauceDemo."""
        # Основной URL сайта SauceDemo
        base_url = 'https://www.saucedemo.com/'

        # Открытие страницы в браузере
        self.driver.get(base_url)

        # Установка размера окна браузера (Full HD разрешение)
        # Это помогает избежать проблем с отображением элементов на маленьких экранах
        self.driver.set_window_size(1920, 1080)

        # Вывод сообщения об успешном открытии страницы
        print("Главная страница успешно открыта")

    def login(self, username, password):
        """Метод для авторизации на сайте SauceDemo."""
        try:
            # Поиск поля для ввода имени пользователя и ввод значения
            self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)

            # Поиск поля для ввода пароля и ввод значения
            self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)

            # Поиск кнопки входа и нажатие на нее
            self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()

            # Вывод сообщения об успешной авторизации
            print("Авторизация прошла успешно")

        except Exception as e:
            # Обработка ошибок при авторизации
            print(f"Ошибка при авторизации: {str(e)}")
            raise  # Повторное выбрасывание исключения для дальнейшей обработки

    def close(self):
        """Метод для закрытия браузера"""
        # Метод quit() закрывает все окна браузера и завершает сеанс WebDriver
        self.driver.quit()
        print("Браузер закрыт")

# Создание экземпляра тестового класса
start_test = TestSauceDemo()

try:
    # Открытие главной страницы
    start_test.open_page()

    # Пауза в 2 секунды для визуальной проверки открытия страницы
    time.sleep(2)

    # Авторизация на сайте с использованием стандартных учетных данных
    start_test.login("standard_user", "secret_sauce")

    # Пауза в 3 секунды для визуальной проверки успешной авторизации
    time.sleep(3)

except Exception as e:
    # Обработка любых ошибок, возникших во время выполнения теста
    print(f"Произошла ошибка во время выполнения теста: {str(e)}")

finally:
    # Закрытие браузера в блоке finally для гарантированного выполнения
    # независимо от того, завершился тест успешно или с ошибкой
    start_test.close()
