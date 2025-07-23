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

# Основной URL сайта, который будет открыт
base_url = 'https://demoqa.com/browser-windows'

# Открытие страницы по указанному URL
driver.get(base_url)

# Нажатие на кнопку для открытия новой вкладки
driver.find_element(By.XPATH, '//button[@id="tabButton"]').click()
print("Click Button New Tab")

# Переключение на новую вкладку
driver.switch_to.window(driver.window_handles[1])
print("Switching to a new tab")
time.sleep(2)

# Возврат на предыдущую вкладку
driver.switch_to.window(driver.window_handles[0])
print("Return to the previous tab")
time.sleep(2)

# Нажатие на кнопку для открытия нового окна
driver.find_element(By.XPATH, '//button[@id="windowButton"]').click()
print("Click Button New Window")
time.sleep(2)

# Переключение на новое окно
driver.switch_to.window(driver.window_handles[2])
print("Switching to a new window")
time.sleep(2)

# Возврат на предыдущее окно
driver.switch_to.window(driver.window_handles[0])
print("Return to the previous window")

# Завершение работы браузера и вывод сообщения об этом
driver.quit()
print("The Chrome browser is closed")