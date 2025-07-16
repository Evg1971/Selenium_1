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
base_url = 'https://www.lambdatest.com/selenium-playground/iframe-demo/'

# Открытие страницы в браузере
driver.get(base_url)

# Поиск элемента iframe по XPath
iframe = driver.find_element(By.XPATH, '//iframe[@id="iFrame1"]')
# Переключение на найденный iframe
driver.switch_to.frame(iframe)

# Поиск поля ввода внутри iframe по XPath
input_pole = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]')
# Выделение всего текста в поле ввода
input_pole.send_keys(Keys.CONTROL + 'a')
# Пауза для ожидания выполнения действий
time.sleep(2)
# Удаление выделенного текста
input_pole.send_keys(Keys.DELETE)
# Пауза для ожидания выполнения действий
time.sleep(2)
# Ввод нового текста в поле
input_pole.send_keys('Interaction with IFrame')
# Выделение всего текста в поле ввода
input_pole.send_keys(Keys.CONTROL + 'a')

# Поиск кнопки Bold на панели редактирования по XPath и клик по ней
click_editing_panel_bold = driver.find_element(By.XPATH, '//button[@title="Bold"]')
click_editing_panel_bold.click()
print("Click editing panel Bold")

# Поиск кнопки Underline на панели редактирования по XPath и клик по ней
click_editing_panel_underline = driver.find_element(By.XPATH, '//button[@title="Underline"]')
click_editing_panel_underline.click()
print("Click editing panel UnderLine")

# Поиск поля ввода после применения стилей по XPath
new_input_pole = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/b/u')
# Получение текста из поля ввода
value_input_pole = new_input_pole.text
# Вывод текста из поля ввода в консоль
print(value_input_pole)
# Пауза для ожидания выполнения действий
time.sleep(2)

# Клик по кнопке Bold на панели редактирования
click_editing_panel_bold.click()
print("Click editing panel Bold")

# Клик по кнопке Underline на панели редактирования
click_editing_panel_underline.click()
print("Click editing panel UnderLine")

# Поиск кнопки Italic на панели редактирования по XPath и клик по ней
driver.find_element(By.XPATH, '//button[@title="Italic"]').click()
print("Click editing panel Italic")

# Поиск кнопки Strike на панели редактирования по XPath и клик по ней
driver.find_element(By.XPATH, '//button[@title="Strike through"]').click()
print("Click editing panel Strike through")

# Поиск поля ввода после применения новых стилей по XPath
new_input_pole_2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/i/strike')
value_input_pole_2 = new_input_pole_2.text

# Проверка, что текст остался тем же после применения стилей
assert value_input_pole == value_input_pole_2, "Editing NOT GOOD"
print("Editing Good")

# Пауза для ожидания выполнения действий перед закрытием браузера
time.sleep(2)

# Завершение работы браузера
driver.quit()
print("The Chrome browser is closed")