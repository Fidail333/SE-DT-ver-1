from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging


class DetalLive:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 15)
        self.original_window = None

    def open_detal_live(self):
        self.browser.get('https://www.sport-express.ru/football/rfpl/online/spartak-fakel-smotret-besplatno-match-20-tura-rpl-v-pryamom-efire-onlayn-tekstovaya-translyaciya-i-rezultat-10-marta-2024-2187914/')

    def menu_nadlogo(self):
        try:
            menu_nadlogo = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')))
            logging.info("Меню найдено")
            return menu_nadlogo
        except TimeoutException:
            return None

    def h1(self):
        try:
            h1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//h1[contains(text(),'«Спартак» — «Факел»: воронежцы вновь обыграли крас')]")))
            logging.info("Заголовок найден")
            return h1
        except TimeoutException:
            return None

    def datelive(self):
        try:
            data = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//div[contains(text(),"10 марта, 21:03")]')))
            logging.info("Время найдено")
            return data
        except TimeoutException:
            return None

    def podval(self):
        try:
            data = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//footer[@class="se-footer"]')))
            logging.info("Подвал найдено")
            return data
        except TimeoutException:
            return None

    def comand(self):
        try:
            comand = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'Положение команд')]")))
            logging.info("Блок положение команд найден")
            return comand
        except TimeoutException:
            return None