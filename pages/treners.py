from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging


class Trener:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.original_window = None

    def open(self):
        self.browser.get('https://www.sport-express.ru/hockey/L/khl/2023-2024/trainers/')

    def menu(self):
        try:
            menu = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')))
            logging.info("Меню найдено и видимо")
            return menu
        except TimeoutException:
            return None


    def treners(self, expected_count=255):
        try:
            player = self.wait.until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, "//td[@class='se-advanced-table-cell']")))
            actual_count = len(player)
            if actual_count == expected_count:
                logging.info(f"Найдено {actual_count} тренеров (ожидалось {expected_count})")
                return True
            else:
                logging.warning(f"Кол-во тренеров:{actual_count} (ожидалось {expected_count})")
                return False
        except TimeoutException:
            logging.error("Не удалось загрузить тренеров")
            return False

    def click_trener(self):
        try:
            click1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//body[1]/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/a[1]")))
            logging.info("Тренер найден и видим")
            click1.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/trainer/477/', "Не правильная ссылка тренера"
            self.browser.back()
            return click1
        except TimeoutException:
            return None

    def knopka(self):
        try:
            for _ in range(40):
                try:
                    knopka = self.browser.find_element(By.XPATH,"//div[@class='se-button']")
                    logging.info("Кнопка с тренером найдена и видна")
                    knopka.click()
                    return knopka
                except:
                    self.browser.execute_script("window.scrollBy(0, 500);")
            logging.info("Кнопка с тренером не найден после прокрутки")
            return None
        except TimeoutException:
            return None

    def click_trn(self):
        try:
            trn = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//tbody/tr[20]/td[2]/a[1]")))
            logging.info("Тренер найден")
            trn.click()
            self.browser.back()
            return trn
        except TimeoutException:
            return None

    def god(self):
        try:
            god = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='css-kxyrhr-control']")))
            logging.info("Селектор сезона найден и видим")
            god.click()

            god2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='css-114a6ms-option' and .='2021-2022']")))
            logging.info("Год в селекторе найден и видим")
            god2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/khl/2021-2022/trainers/', "Не правильный урл года"
            return god2
        except TimeoutException:
            return None

    def h1(self):
        try:
            h1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//h1[contains(text(),'Тренеры')]")))
            logging.info("Заголовок найден")
            return h1
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
