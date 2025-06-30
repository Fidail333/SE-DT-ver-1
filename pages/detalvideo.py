from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import logging


class DetalVideo:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 15)
        self.original_window = None


    def open_detal_video(self):
        self.browser.get('https://www.sport-express.ru/hockey/khl/videoreports/aleksandr-hmelevskiy-vylet-salavata-seriya-s-traktorom-buduschee-v-klube-intervyu-2188513/')

    def menu_nadlogo(self):
        try:
            menu_nadlogo = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')))
            logging.info("Меню найдено и видно")
            return menu_nadlogo
        except TimeoutException:
            return None

    def h1(self):
        try:
            h1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//h1[contains(text(),'Хмелевский: вылет «Салавата», серия с «Трактором»,')]")))
            logging.info("Заголовок найден")
            return h1
        except TimeoutException:
            return None

    def rekalama(self):
        try:
            reklama = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@id='adfox_15645683733586888']")))
            logging.info("Реклама найдена")
            return reklama
        except TimeoutException:
            return None

    def date(self):
        try:
            date = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//p[@class='se-material-page__date']")))
            logging.info("Дата и время найдены и отображаются")
            return date
        except TimeoutException:
            return None

    def bread(self):
        try:
            bread = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[@href='/hockey/']")))
            logging.info("Крошки выводятся")
            bread.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/hockey/', "Не правильный переход в хоебные крошки"
            self.browser.back()
            return bread
        except TimeoutException:
            return None

    def stadion(self):
        try:
            stadion = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='se-menu-subtop__link']")))
            ActionChains(self.browser).move_to_element(stadion).perform()
            logging.info("Курсор наведен на элемент меню")
            stadion2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Стадионы')]")))
            stadion2.click()
            sleep(2)
            assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/khl/2024-2025/stadiums/', "Не правильная ссылка стадионов"
            logging.info("Вторая кнопка найдена и нажата")
            return stadion2
        except TimeoutException:
            return None