# Импорт основного класса webdriver для управления браузером
from selenium import webdriver
# Импорт классов для работы с ожиданиями элементов
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Импорт класса Service для настройки сервиса ChromeDriver
from selenium.webdriver.chrome.service import Service as ChromeService
# Импорт класса By для поиска элементов по различным локаторам
from selenium.webdriver.common.by import By
# Импорт менеджера драйверов для автоматической установки ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager
# Импорт конкретных исключений для обработки ошибок
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from login_page import LoginPage

class Test:
    """Класс для тестирования сайта SauceDemo."""
    # Глобальные переменные с XPath продуктов (классовые атрибуты)
    # Хранит XPath для кнопок добавления товаров в корзину
    PRODUCT_XPATHS = {
        'backpack': "//button[@id='add-to-cart-sauce-labs-backpack']",
        'bike_light': "//button[@id='add-to-cart-sauce-labs-bike-light']",
        'bolt_t_shirt': "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']",
        'fleece_jacket': "//button[@id='add-to-cart-sauce-labs-fleece-jacket']",
        'onesie': "//button[@id='add-to-cart-sauce-labs-onesie']",
        'red_t_shirt': "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
    }
    # Локаторы для элементов страницы
    LOGIN_LOCATORS = {
        'button_to_cart': (By.XPATH, "//span[@class='shopping_cart_badge']"),
        'button_your_cart': (By.XPATH, "//span[@class='title']")
        }

    def __init__(self):
        """Конструктор класса. Инициализирует драйвер Chrome с необходимыми опциями."""
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

    def open_page_and_authorization(self, url="https://www.saucedemo.com", width=1920, height=1080):
        """Метод для открытия веб-страницы."""
        try:
            # Открытие страницы в браузере по указанному URL
            self.driver.get(url)
            # Установка размера окна браузера
            self.driver.set_window_size(width, height)
            # Вывод сообщения об успешном открытии страницы
            print(f"Страница {url} успешно открыта с разрешением {width}x{height}")
            # Создаем экземпляр класса LoginPage, передавая драйвер в конструктор
            login = LoginPage(self.driver)
            # Вызываем метод authorization для выполнения авторизации с указанными именем пользователя и паролем
            login.authorization(login_name='standard_user', login_password='secret_sauce')
        except NoSuchElementException as e:
            # Обработка ошибки, если элемент не найден
            print(f"Элемент не найден: {str(e)}")
            raise

    def add_product_to_cart(self, product_key):
        """Добавление продукта в корзину."""
        try:
            # Получаем XPath для указанного продукта
            product_xpath = self.PRODUCT_XPATHS.get(product_key)
            # Проверяем, что ключ существует в словаре
            if product_xpath is None:
                raise ValueError(
                    f"Неизвестный ключ продукта: {product_key}. "
                    f"Доступные ключи: {list(self.PRODUCT_XPATHS.keys())}"
                )
            # Используем явное ожидание для кнопки добавления в корзину
            add_to_cart_button = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, product_xpath))
            )
            # Кликаем по кнопке добавления в корзину
            add_to_cart_button.click()
            # Вывод сообщения об успешном добавлении
            print(f"Товар {product_key} добавлен в корзину")
        except NoSuchElementException as e:
            # Обработка ошибки, если элемент не найден
            print(f"Элемент не найден: {str(e)}")
            raise
        except TimeoutException as e:
            # Обработка ошибки таймаута
            print(f"Таймаут ожидания элемента: {str(e)}")
            raise

    def transfer_to_cart_and_check(self):
        """Переход в корзину и проверка, что мы находимся в корзине."""
        try:
            # Создаем объект ожидания с таймаутом 30 секунд
            wait = WebDriverWait(self.driver, 30)
            # Ожидаем и находим кнопку корзины
            cart_button = wait.until(
                EC.element_to_be_clickable(self.LOGIN_LOCATORS["button_to_cart"])
            )
            # Кликаем по кнопке корзины
            cart_button.click()
            print("Переход в корзину прошел успешно")
            # Ожидаем и находим заголовок "Your Cart"
            title_your_cart = wait.until(
                EC.element_to_be_clickable(self.LOGIN_LOCATORS["button_your_cart"])
            )
            # Проверяем, что текст элемента равен "Your Cart"
            assert title_your_cart.text == "Your Cart", f"Ожидался текст 'Your Cart', но получен: {title_your_cart.text}"
            # Вывод сообщения об успешном завершении теста
            print("Тест завершен успешно")
        except NoSuchElementException as e:
            # Обработка ошибки, если элемент не найден
            print(f"Элемент не найден: {str(e)}")
            raise
        except TimeoutException as e:
            # Обработка ошибки таймаута
            print(f"Таймаут ожидания элемента: {str(e)}")
            raise
        except AssertionError as e:
            # Обработка ошибки утверждения
            print(f"Проверка не пройдена: {str(e)}")
            raise

    def close(self):
        """Метод для закрытия браузера."""
        try:
            # Закрываем браузер и завершаем сеанс WebDriver
            self.driver.quit()
            print("Браузер успешно закрыт")
        except WebDriverException as e:
            # Обработка ошибок при закрытии браузера
            print(f"Ошибка при закрытии браузера: {str(e)}")
            raise

# Создание экземпляра тестового класса
test_site = Test()
try:
    # Открытие главной страницы
    test_site.open_page_and_authorization()
    # Добавление товара в корзину
    test_site.add_product_to_cart('bike_light')
    # Переход в корзину и проверка
    test_site.transfer_to_cart_and_check()
except TimeoutException as e:
    # Обработка ошибки таймаута
    print(f"Таймаут ожидания элемента: {str(e)}")
    raise
except WebDriverException as e:
    # Обработка общих ошибок WebDriver
    print(f"Ошибка при авторизации: {str(e)}")
    raise
finally:
    # Закрытие браузера в блоке finally для гарантированного выполнения
    test_site.close()
