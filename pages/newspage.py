from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging


class NewsPage:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.original_window = None


    def open(self):
        self.browser.get('https://www.sport-express.ru/news/')

    def h1_news(self):
        try:
            h1_news = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//h1[contains(text(),"Весь спорт.")]')))
            logging.info("Заголовок найден и виден")
            return h1_news
        except TimeoutException:
            return None

    def button_main(self):
        try:
            button1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//a[contains(text(),"Главные")]')))
            logging.info("Кнопка найдена и видна")
            button1.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/news/?isEditorialChoice=1', "Неверный урл Главные кнопки"
            return button1
        except TimeoutException:
            return None

    def button_readers(self):
        try:
            button2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//a[contains(text(),"Выбор читателей")]')))
            logging.info("Кнопка найдена и видна")
            button2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/news/?isHot=1', "Не верный урл Выбор читателей"
            return button2
        except TimeoutException:
            return None

    def button_exclusive(self):
        try:
            button3 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Эксклюзив')]")))
            logging.info("Кнопка найдена и видна")
            button3.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/news/?isExclusive=1', "Не верный урл кнопки эксклюз"
            return button3
        except TimeoutException:
            return None

    def reviews_vid(self):
        try:
            reviews_vid = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[@class='se-material-filter-headline__item']")))
            logging.info("Кнопка статьи найдена и видна")
            reviews_vid.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/reviews/', "Не правильная кнопка статьи"
            self.browser.back()
            return reviews_vid
        except TimeoutException:
            return None

    def football_button(self):
        try:
            football_button = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'''//a[contains(@class,'se-material-filter-menu__item-button')][contains(text(),"Футбол")]''')))
            logging.info("Кнопка найдена и видна")
            football_button.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/football/news/', "Не правильный урл кнопки Футбол"
            return football_button
        except TimeoutException:
            return None

    def h1_football_news(self):
        try:
            h1_football_news = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//h1[contains(text(),"Новости футбола")]')))
            logging.info("Кнопка найдена и видна")
            return h1_football_news
        except TimeoutException:
            return None

    def reviews(self,expected_count=30):
        try:
            reviews = self.wait.until(
                EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='se-news-list-page__item']")))
            actual_count = len(reviews)
            if actual_count == expected_count:
                logging.info(f"Найдено {actual_count} статей (ожидалось {expected_count})")
                return True
            else:
                logging.warning(f"Кол-во статей:{actual_count} (ожидалось {expected_count})")
                return False
        except TimeoutException:
            logging.error("Не удалось загрузить список статей")
            return False

    def cup_selector(self):
        try:
            cup_selector = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//div[@class="se-select se-select--1col se-select--selected se-select--theme-sky"]')))
            logging.info("Селектор найден и виден")
            cup_selector.click()
            return cup_selector
        except TimeoutException:
            logging.info("Селектор не найден")
            return None

    def cup_rpl(self):
        try:
            cup_rpl = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='se-select__items']//div[3]")))
            logging.info("Селектор найден и виден")
            cup_rpl.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/football/rfpl/news/', "Не правильный турнир"
            return cup_rpl
        except TimeoutException:
            return None

    def reklama_block(self):
        try:
            reklama_block = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@id='adfox_15645683733586888']")))
            logging.info("Реклама найдена")
            return reklama_block
        except TimeoutException:
            return None