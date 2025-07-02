import time

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Настройка опций Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Эта опция предотвращает
# автоматическое закрытие браузера после завершения скрипта

# Создание экземпляра драйвера
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)
# Основной URL
base_url = 'https://menonparik.github.io/double-click-tester/'

# Открытие страницы
driver.get(base_url)

#Создание экземпляра ActionChains
action = ActionChains(driver)

#Поиск кнопки "click" по XPATH
click_button = driver.find_element(By.XPATH, '//button[@id="click"]')

#Выполнение двойного клика по кнопке
action.double_click(click_button).perform()
print("Double click was made")  # Информация о том, что двойной клик выполнен

#Получение текста элемента, который показывает количество двойных кликов
value_double_click_button = driver.find_element(By.XPATH, '//span[@id="doubleclickleft"]').text

#Проверка, что количество двойных кликов соответствует ожидаемому значению
assert "Double Clicks: 1" == f"Double Clicks: {value_double_click_button}", "No double click was made"
print("Double Click Good")

#Пауза в 2 с
time.sleep(2)

#Выполнение правого клика по кнопке и вывод информации об этом
action.context_click(click_button).perform()
print("Right key was clicked")

#Получение текста элемента, который показывает количество правых кликов
value_right_click_button = driver.find_element(By.XPATH, '//span[@id="clickright"]').text

#Проверка, что количество правых кликов соответствует ожидаемому значению
assert "Clicks: 1" == f"Clicks: {value_right_click_button}", "No right-click was made"
print("Right Click Good") # Информация о том, что правый клик зарегистрирован

time.sleep(2) #Задержка на 2 секунды перед завершением работы
#Завершение работы браузера
driver.quit()
print("The Chrome browser is closed")