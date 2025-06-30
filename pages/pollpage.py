import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class PollPage:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 15)
        self.original_window = None


    def open_poll(self):
        self.browser.get('https://www.sport-express.ru/poll/')

    def h1_poll(self):
        try:
            h1_poll = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//h1[contains(text(),"Весь спорт.")]')))
            logging.info("Заголовок найден")
            return h1_poll
        except TimeoutException:
            return None

    def eshe(self):
        try:
            eshe = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='se-material-filter-menu__item-button ']")))
            time.sleep(15)
            eshe.click()
            logging.info("Кнопка найдена и нажата")
            eshe2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='/volleyball/poll/']")))
            eshe2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/volleyball/poll/', "Не правильный урл"
            logging.info("Вторая кнопка найдена и нажата")
            return eshe2
        except TimeoutException:
            return None

    def reviews(self,expected_count=30):
        try:
            reviews = self.wait.until(
                EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='se-news-list-page__item-right']")))
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


    def material(self):
        try:
            material = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Россия — Франция в финалах Олимпиады в мужском вол')]")))
            logging.info("материал найден")
            material.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/olympics/tokyo2020/poll/rossiya-franciya-v-finalah-olimpiady-v-muzhskom-voleybole-i-zhenskom-gandbole-kto-pobedit-1821332/', "Не правильный урл"
            return material
        except TimeoutException:
            return None

