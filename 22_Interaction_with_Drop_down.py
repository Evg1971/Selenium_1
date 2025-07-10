# Импорт модуля time для использования функций, связанных со временем
import time
# Импорт класса Keys из модуля selenium.webdriver для имитации нажатия клавиш
from selenium.webdriver import Keys
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
base_url = 'https://lambdatest.com/selenium-playground/jquery-dropdown-search-demo'

# Открытие страницы в браузере
driver.get(base_url)

# Поиск элемента выпадающего списка по XPath и клик по нему
click_drop = driver.find_element(By.XPATH, '//span[@aria-labelledby="select2-country-container"]')
click_drop.click()

time.sleep(3) # Пауза в 3 секунды

# Поиск поля ввода для страны по XPath
input_country = driver.find_element(By.XPATH, '(//input[@class="select2-search__field"])[2]')
# Ввод текста "India" в поле ввода
input_country.send_keys("India")

time.sleep(3)

# Имитация нажатия клавиши RETURN (Enter) для выбора страны
input_country.send_keys(Keys.RETURN)
