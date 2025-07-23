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
base_url = 'https://the-internet.herokuapp.com/javascript_alerts'

# Открытие страницы по указанному URL
driver.get(base_url)

# Нажатие на кнопку для вызова JS Alert
driver.find_element(By.XPATH, '//button[@onclick="jsAlert()"]').click()
print("Click JS Alert Button")
time.sleep(2)

# Подтверждение алерта
driver.switch_to.alert.accept()

# Проверка результата после нажатия на JS Alert
result_alert = "You successfully clicked an alert"
value_result_alert = driver.find_element(By.XPATH, '//p[@id="result"]').text
assert result_alert == value_result_alert, "Incorrect clicked an alert"
print("Click Button JS Alert Good")

# Нажатие на кнопку для вызова JS Confirm
driver.find_element(By.XPATH, '//button[@onclick="jsConfirm()"]').click()
print("Click JS Confirm Button")
time.sleep(2)

# Отмена подтверждения алерта
driver.switch_to.alert.dismiss()

# Проверка результата после нажатия на JS Confirm
result_confirm_cancel = "You clicked: Cancel"
value_result_confirm_cancel = driver.find_element(By.XPATH, '//p[@id="result"]').text
assert result_confirm_cancel == value_result_confirm_cancel, "Incorrect clicked a confirm"
print("Click Button JS Confirm Good")

# Нажатие на кнопку для вызова JS Prompt
driver.find_element(By.XPATH, '//button[@onclick="jsPrompt()"]').click()
print("Click JS Prompt Button")
time.sleep(2)

# Ввод текста в алерт и подтверждение
driver.switch_to.alert.send_keys("JS_Prompt")
time.sleep(2)
driver.switch_to.alert.accept()

# Проверка результата после нажатия на JS Prompt
result_prompt = "You entered: JS_Prompt"
value_prompt = driver.find_element(By.XPATH, '//p[@id="result"]').text
assert result_prompt == value_prompt, "Incorrect click button JS Prompt"
print("Click Button JS Prompt Good")

# Завершение работы браузера и вывод сообщения об этом
driver.quit()
print("The Chrome browser is closed")