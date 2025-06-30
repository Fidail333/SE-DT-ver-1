import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class OnlinePage:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 15)
        self.original_window = None


    def open_online(self):
        self.browser.get('https://www.sport-express.ru/online/')


    def h1_online(self):
        try:
            h1_online = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//h1[contains(text(),'Весь спорт.')]")))
            logging.info("Заголовок найден")
            return h1_online
        except TimeoutException:
            return None


    def eshe(self):
        try:
            eshe = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='se-material-filter-menu__item-button ']")))
            time.sleep(15)
            eshe.click()
            logging.info("Кнопка найдена и нажата")
            eshe2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[@href='/tennis/online/']")))
            eshe2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tennis/online/', "Не правильный урл"
            logging.info("Вторая кнопка найдена и нажата")
            return eshe2
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



