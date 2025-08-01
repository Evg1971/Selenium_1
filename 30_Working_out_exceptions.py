# Импорт модуля time для использования функций, связанных со временем, таких как sleep
import time
# Импорт модуля webdriver из selenium для управления браузером
from selenium import webdriver
# Импорт класса Service из модуля selenium.webdriver.chrome.service для управления сервисом ChromeDriver
from selenium.webdriver.chrome.service import Service as ChromeService
# Импорт класса By из модуля selenium.webdriver.common.by для поиска элементов на странице
from selenium.webdriver.common.by import By
# Импорт класса ChromeDriverManager из модуля webdriver_manager.chrome для автоматического управления драйвером Chrome
from webdriver_manager.chrome import ChromeDriverManager
# Импорт класса NoSuchElementException из модуля selenium.common.exceptions для обработки исключения "Элемент не найден"
from selenium.common.exceptions import NoSuchElementException

# Настройка опций Chrome
options = webdriver.ChromeOptions()  # Создание объекта опций для настройки параметров браузера Chrome

# Добавление экспериментальной опции для предотвращения автоматического закрытия браузера после завершения скрипта
options.add_experimental_option("detach", True)

# Создание экземпляра драйвера Chrome с указанными опциями и сервисом
# ChromeDriverManager автоматически скачивает и настраивает нужную версию драйвера Chrome
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# Основной URL для тестирования - страница с динамическими элементами
base_url = 'https://demoqa.com/dynamic-properties'

# Открытие страницы в браузере по указанному URL
driver.get(base_url)

# Блок try-except для обработки исключения, когда элемент не найден
try:
    # Попытка найти кнопку с ID "visibleAfter" и нажать на нее
    # Эта кнопка становится видимой только через 5 секунд после загрузки страницы
    print("Attempt to click the button 'Visible After 5 Seconds' immediately after loading the page")
    button_visible = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
    button_visible.click()  # Нажатие на найденную кнопку
    print("The button was found and clicked immediately after the page was loaded - this is unexpected")

# Обработка исключения NoSuchElementException, которое возникает, когда элемент не найден на странице
except NoSuchElementException:
    # Вывод сообщения об ошибке
    print("Received NoSuchElementException - this is the expected behavior")

        # Обновление страницы для повторной попытки
    driver.refresh()
    print("Page reload")

    # Ожидание 5 секунд, чтобы кнопка стала видимой
    print("Waiting 5 seconds for the button to appear...")
    time.sleep(5)

    # Повторная попытка найти кнопку после ожидания и обновления страницы
    button_visible = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')

    # Нажатие на найденную кнопку
    button_visible.click()

    # Вывод сообщения об успешном нажатии кнопки
    print("Click Button Visible")
# Завершение работы браузера и вывод сообщения об этом
finally:
    driver.quit()
    print("The Chrome browser is closed")