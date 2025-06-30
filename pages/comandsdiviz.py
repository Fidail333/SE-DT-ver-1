from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class ComandDiviz:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.original_window = None

    def open(self):
        self.browser.get('https://www.sport-express.ru/hockey/L/khl/2024-2025/teams/')

    def deviz(self, expected_count=4):
        try:
            player = self.wait.until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, "//div[@class='sp-competition-teams__group-title']")))
            actual_count = len(player)
            if actual_count == expected_count:
                logging.info(f"Найдено {actual_count} девизионов (ожидалось {expected_count})")
                return True
            else:
                logging.warning(f"Кол-во девезионов:{actual_count} (ожидалось {expected_count})")
                return False
        except TimeoutException:
            logging.error("Не удалось загрузить девезионов")
            return False

    def comands(self):
        try:
            comands1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='sp-competition-teams']//div[1]//div[1]//div[2]//div[1]//div[1]//div[2]//div[2]//a[1]")))
            logging.info("Состав найден")
            comands1.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/cska-hokkey-313/players/', "Не правильный урл состава"
            self.browser.back()

            comands2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='sp-competition-teams']//div[1]//div[2]//div[2]//div[1]//div[1]//div[2]//div[2]//a[2]")))
            logging.info("Календарь найден")
            comands2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/khl/2024-2025/calendar/?team=6',"Не правильный урл календаря"
            self.browser.back()

            comands3 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='sp-competition-teams']//div[1]//div[1]//div[2]//div[2]//div[1]//div[2]//div[2]//a[3]")))
            logging.info("Все найдено")
            comands3.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/severstal-hokkey-758/players-stats/', "Не правильный урл статистики"
            self.browser.back()
            return comands3
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

    def data(self):
        try:
            data = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='css-kxyrhr-control']")))
            logging.info("Селектор выбора сезона найден")
            data.click()

            data2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//div[@class="css-114a6ms-option" and text()="2021-2022"]')))
            logging.info("Дата 2020 найдена и видима")
            data2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/khl/2021-2022/teams/', "Не правильный урл 20 года"
            return data2
        except TimeoutException:
            return None

    def h1(self):
        try:
            h1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//h1[contains(text(),'FONBET')]")))
            logging.info("Заголовок найден")
            return h1
        except TimeoutException:
            return None







    def knopki(self):
        knopki = self.browser.find_element(By.XPATH,"//div[@class='sp-competition-teams']//div[1]//div[2]//div[2]//div[5]//div[1]//div[2]//div[2]")

    def spartak(self):
        spartak = self.browser.find_element(By.XPATH, "//img[@title='Спартак']")
        spartak.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/spartak-hokkey-513/', "Не правильный урл спартака"
        self.browser.back()

    def filtri(self):
        filtri = self.browser.find_element(By.XPATH,"//div[@class='css-kxyrhr-control']")
        filtri.click()
