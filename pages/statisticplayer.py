from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging


class StatisticPlayer:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.original_window = None

    def open(self):
        self.browser.get('https://www.sport-express.ru/football/L/player/56936/seasons/2023-2024/')

    def menu(self):
        try:
            menu = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')))
            logging.info("Менб видно и нашлось")
            return menu
        except TimeoutException:
            return None

    def info(self):
        try:
            info1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//b[contains(text(),'Армения')]")))
            logging.info("Инфо найдено")

            info2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//b[normalize-space()='07.06.2000']")))
            logging.info("Вся инфа найдена")
            return info2
        except TimeoutException:
            return None

    def match(self):
        try:
            match1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//td[normalize-space()='07.06.2024']")))
            logging.info("Матч 2024 найден")

            match2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//td[normalize-space()='21.07.2023']")))
            logging.info("матч 2023 найден")
            return match2
        except TimeoutException:
            return None

    def reklama(self):
        try:
            reklama = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@id='adfox_15645683733586888']")))
            logging.info("Реклама найдена")
            return reklama
        except TimeoutException:
            return None

    def apponent(self):
        try:
            appon = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Соперники')]")))
            logging.info("Кнопка сопреники найдена и видна")
            appon.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/football/L/player/56936/rivals/', "Не правильная ссылка соперников"
            return appon
        except TimeoutException:
            return None