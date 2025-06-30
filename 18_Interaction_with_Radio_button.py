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
# Находим радиокнопку "Последний" и проверяем, что она выбрана
value_radio_button = driver.find_element(By.XPATH, '//*[@id="radio-group-react"]/div/div[1]/div/span[2]/div/div/span/span/div/div[5]/label/input')
assert value_radio_button.is_selected(), "Radio Button Последний is NOT selected"
print(f"Radio Button {radio_button.text} is selected")
time.sleep(2)
#Завершение работы браузера
driver.quit()
print("The Chrome browser is closed")
