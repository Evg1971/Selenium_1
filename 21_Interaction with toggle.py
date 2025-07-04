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
base_url = 'https://practice-automation.com/slider/'

# Открытие страницы
driver.get(base_url)

#Создаем объект ActionChains для выполнения взаимодействий с элементами
actions = ActionChains(driver)

#Находим слайдер на странице по его идентификатору
slider = driver.find_element(By.XPATH, '//input[@id="slideMe"]')

time.sleep(3)

#Удерживаем ползунок слайдера, перемещаем его на 100 пикселей вправо и затем отпускаем
actions.click_and_hold(slider).move_by_offset(100, 0).release().perform()
print("The slider has been moved") #Вывод сообщения о том, что слайдер был перемещен

#Находим текстовое значение текущего положения слайдера
value_slider = driver.find_element(By.XPATH, '//span[@id="value"]').text

#Проверяем, что значение слайдера равно ожидаемому значению "Current value: 60"
assert "Current value: 60" == f"Current value: {value_slider}", "Value Slider Incorrect"

#Вывод сообщения об успешном перемещении слайдера
print("Move the Slider Good")