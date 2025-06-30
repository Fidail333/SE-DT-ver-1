from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
from selenium.webdriver.support.ui import Select


class TenisMatch:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.original_window = None

    def open(self):
        self.browser.get('https://www.sport-express.ru/tennis/L/atp/')

    def menu(self):
        try:
            menu = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')))
            logging.info("Меню найдено и видно")
            return menu
        except TimeoutException:
            return None

    def name_of_turnir(self):
        try:
            name = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//tbody/tr[10]/td[2]/a[1]")))
            logging.info("Название турнира найдено")
            name.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tennis/L/atp/montpellier/2025/', "Не правильный урл турнира"

            name2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Александр Ковачевич (США)')]")))
            logging.info("матч найден")
            self.browser.back()
            return name2
        except TimeoutException:
            return None

    def reklama(self):
        try:
            reklama = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@id='adfox_15645683733586888']")))
            logging.info("Реклама найдена и видна")
            return reklama
        except TimeoutException:
            return None

    def selector(self):
        try:
            select = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//select[@class='common_height_26 mb_10']")))
            logging.info("Селектор выбора сезона найден и видим")
            select = Select(select)
            select.select_by_index(5)
            assert self.browser.current_url == 'https://www.sport-express.ru/tennis/L/atp/2020/', "Не правильный урл"
            return select
        except TimeoutException:
            return None

    def vibor(self):
        try:
            vibor = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//tbody/tr[4]/td[2]/a[1]")))
            logging.info("Турнир найден")
            vibor.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tennis/L/atp/adelaide/2020/', "Не правильный урл"
            return vibor
        except TimeoutException:
            return None

