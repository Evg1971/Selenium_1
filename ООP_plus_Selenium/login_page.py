# Импорт классов для работы с ожиданиями элементов
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Импорт класса By для поиска элементов по различным локаторам
from selenium.webdriver.common.by import By
# Импорт конкретных исключений для обработки ошибок
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException

class LoginPage():
    # Локаторы для элементов страницы
    LOGIN_LOCATORS = {
        'username': (By.XPATH, "//input[@placeholder='Username']"),
        'password': (By.XPATH, "//input[@placeholder='Password']"),
        'login_button': (By.XPATH, "//input[@id='login-button']"),
    }

    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, login_password):
        """Метод для авторизации на сайте с использованием явных ожиданий."""
        try:
            # Создаем объект ожидания с таймаутом 30 секунд
            wait = WebDriverWait(self.driver, 30)
            # Ожидаем и находим поле для ввода имени пользователя
            username_field = wait.until(
                EC.element_to_be_clickable(self.LOGIN_LOCATORS["username"])
            )
            # Очищаем поле перед вводом (на случай если там уже есть текст)
            username_field.clear()
            # Вводим имя пользователя
            username_field.send_keys(login_name)
            # Ожидаем и находим поле для ввода пароля
            password_field = wait.until(
                EC.element_to_be_clickable(self.LOGIN_LOCATORS["password"])
            )
            # Очищаем поле перед вводом
            password_field.clear()
            # Вводим пароль
            password_field.send_keys(login_password)
            # Ожидаем и находим кнопку входа
            login_button = wait.until(
                EC.element_to_be_clickable(self.LOGIN_LOCATORS["login_button"])
            )
            # Кликаем по кнопке входа
            login_button.click()
            # Вывод сообщения об успешной авторизации
            print("Авторизация прошла успешно")
        except NoSuchElementException as e:
            # Обработка ошибки, если элемент не найден
            print(f"Элемент не найден: {str(e)}")
            raise
        except TimeoutException as e:
            # Обработка ошибки таймаута
            print(f"Таймаут ожидания элемента: {str(e)}")
            raise
        except WebDriverException as e:
            # Обработка общих ошибок WebDriver
            print(f"Ошибка при авторизации: {str(e)}")
            raise
