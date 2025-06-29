import time

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
base_url = 'https://guides.kontur.ru/components/selection-elements/radio/'

# Открытие страницы
driver.get(base_url)
# Добавляем задержку в 1 секунду для ожидания загрузки элементов
time.sleep(1)
# Находим и кликаем по тексту "Последний" напротив радиокнопки
radio_button = driver.find_element(By.XPATH, '//*[@id="radio-group-react"]/div/div[1]/div/span[2]/div/div/span/span/div/div[5]/label/div')
radio_button.click()
# Сохраняем текст заголовка в переменную для проверки
text_radio_button = radio_button.text
assert text_radio_button == "Последний"
# Выводим сообщение об успешной проверке заголовка радиокнопки
print(f"Выбрана радиокнопка {text_radio_button} корректно")