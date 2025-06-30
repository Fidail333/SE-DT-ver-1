from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class DetalNews:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 15)
        self.original_window = None


    def open_detal_news(self):
        self.browser.get('https://www.sport-express.ru/football/rfpl/news/eks-prezident-lokomotiva-naumov-ocenil-igru-dzyuby-i-suleymanova-2188563/')

    def menu_nadlogo(self):
        try:
            menu_nadlogo = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')))
            logging.info("Меню найдено и видно")
            return menu_nadlogo
        except TimeoutException:
            return None

    def h1(self):
        try:
            h1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//h1[contains(text(),'Экс-президент «Локомотива»: «Галактионов прав. Дзю')]")))
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

    def autor(self):
        try:
            autor = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='se-author__main']")))
            logging.info("Автор найден")
            return autor
        except TimeoutException:
            return None

    def comand(self):
        try:
            comand = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='se-author__main']")))
            logging.info("Положение команд - найдено")
            return comand
        except TimeoutException:
            return None

    def block_news(self):
        try:
            for _ in range(20):
                try:
                   block_news = self.browser.find_element(By.XPATH,"//div[contains(text(),'Новости')]")
                   logging.info("Блок с новостями найден")
                   return block_news
                except:
                    self.browser.execute_script("window.scrollBy(0, 500);")
            logging.error("Блок не найден после прокрутки")
            return None
        except TimeoutException:
            return None

    def obsh(self):
        try:
            obsh = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='se-readers-choice__title']")))
            logging.info("Блок самые обсуждаемые выводится")
            return obsh
        except TimeoutException:
            return None

    def table(self):
        try:
            table = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Таблица переходов')]")))
            logging.info("Кнопка таблица переходов найдена!")
            table.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/football/rfpl/reviews/rpl-tablica-perehodov-2025-vse-transfery-kto-ushel-i-prishel-krasnodar-zenit-cska-spartak-dinamo-lokomotiv-sdelki-onlayn-2330090/', "Не правильный урл таблицы"
            return table
        except TimeoutException:
            return None

    def footer(self):
        try:
            footer = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//footer[@class='se-footer']")))
            logging.info("Подвал найден")
            return footer
        except TimeoutException:
            return None


    def block_comment(self):
        try:
            for _ in range(500):
                try:
                   block_comment = self.browser.find_element(By.XPATH,"//div[@placeholder='Оставьте комментарий']")
                   logging.info("Блок с комментами найден")
                   return block_comment
                except:
                    self.browser.execute_script("window.scrollBy(0, 1500);")
                    sleep(2)
            logging.error("Блок не найден после прокрутки")
            return None
        except TimeoutException:
            return None