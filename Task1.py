from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
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
base_url = 'https://saucedemo.com/'

# Открытие страницы
driver.get(base_url)

# Установка размера окна
driver.set_window_size(1920, 1080)

