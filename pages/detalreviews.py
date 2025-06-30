from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging


class DetalReviews:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 15)
        self.original_window = None

    def open_detal_reviews(self):
        self.browser.get('https://www.sport-express.ru/football/rfpl/reviews/lokomotiv-sygral-vnichyu-s-sochi-mnenie-byvshego-prezidenta-zheleznodorozhnikov-nikolaya-naumova-o-matche-2188444/')

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
                EC.visibility_of_element_located((By.XPATH,"//h1[contains(text(),'«Галактионов прав. Дзюба — не игрок стартового сос')]")))
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
                EC.visibility_of_element_located((By.XPATH,"//div[@class='se-author se-author--alone']")))
            logging.info("Автор найден")
            return autor
        except TimeoutException:
            return None

    def comand(self):
        try:
            comand = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'Положение команд')]")))
            logging.info("Положение команд - найдено")
            return comand
        except TimeoutException:
            return None

    def tags(self):
        try:
            tags = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Артем Дзюба')]")))
            logging.info("Теги найдены")
            tags.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/artem-dzyuba-132/', "Не правильный дзюба"
            self.browser.back()
            return tags
        except TimeoutException:
            return None

    def like(self):
        try:
            like = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='se-reaction se-reaction--theme-row']")))
            logging.info("Лайки найдены")
            return like
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

    def calendar(self):
        try:
            calendar = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'''//a[@class='se-menu-subtop__link'][contains(text(),"Календарь")]''')))
            logging.info("Каленадрь найден")
            calendar.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/football/L/russia/premier/2025-2026/calendar/tours/', "Не правильный урл календаря"
            return calendar
        except TimeoutException:
            return None
