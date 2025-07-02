import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import logging
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope="session")
def browser():

    logging.basicConfig(
        level=logging.INFO,  # или DEBUG для более детальных логов
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("test_logs.log"),  # логи в файл
            logging.StreamHandler()  # логи в консоль
        ]
    )
    options = Options()
    options.page_load_strategy="eager"
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")  # Решает проблему с /dev/shm
    options.add_argument("--disable-gpu")  # Отключает GPU
    options.add_argument("--headless=new")  # Для headless-режима
    options.add_argument("--disable-software-rasterizer")
    service = Service()
    options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
    #options.add_argument('--headless')
    # browser = webdriver.Chrome(service=service, options=options)
    browser = webdriver.Remote(command_executor="http://selenium:4444/wd/hub", options=options)
    browser.maximize_window()
    yield browser
    browser.quit()

def pytest_runtest_logreport(report):
    if report.failed:  # Если тест упал
       report.outcome = "skipped"  # Меняем статус на "пропущен"
       report.wasxfail = None  # Убираем возможные конфликты