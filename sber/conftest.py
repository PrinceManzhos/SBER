import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Config:
    # Здесь определите настройки вашей конфигурации, если значение 'ci' используется в вашем проекте
    ENV = "ci1"

@pytest.fixture()
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    if Config.ENV == 'ci':
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=1280,720")
    chrome_options.add_argument("start-maximized")

    # Используйте ChromeDriverManager для автоматического скачивания нужной версии драйвера
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()
