from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class Nakazanie:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.original_window = None

    def open(self):
        self.browser.get('https://www.sport-express.ru/football/L/russia/first/2024-2025/statistics/cards/')

    def menu_ndalogo(self):
        try:
            menu = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')))
            logging.info("Меню найдено")
            return menu
        except TimeoutException:
            return None

    def player(self):
        try:
            player = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Илья Сафронов')]")))
            logging.info("Игрок найден и виден")
            player.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/football/L/player/48845/seasons/2024-2025/', "Не правильный игрок"
            self.browser.back()
            return player
        except TimeoutException:
            return None

    def reklama(self):
        try:
            reklama = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@id='adfox_15645683733586888']")))
            logging.info("реклама найдена и видна")
            return reklama
        except TimeoutException:
            return None









