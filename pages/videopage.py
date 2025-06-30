from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging


class VideoPage:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 17)
        self.original_window = None


    def open_video(self):
        self.browser.get('https://www.sport-express.ru/videoreports/')


    def h1_video(self):
        try:
            h1_video = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//h1[contains(text(),'Видео')]")))
            logging.info("Заголовок найден")
            return h1_video
        except TimeoutException:
            return None

    def button_main(self):
        try:
            button1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//a[contains(text(),"Главные")]')))
            logging.info("Кнопка найдена и видна")
            button1.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/videoreports/?isEditorialChoice=1', "Неверный урл Главные кнопки"
            return button1
        except TimeoutException:
            return None

    def button_readers(self):
        try:
            button2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//a[contains(text(),"Выбор читателей")]')))
            logging.info("Кнопка найдена и видна")
            button2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/videoreports/?isHot=1', "Не верный урл Выбор читателей"
            return button2
        except TimeoutException:
            return None

    def button_exclusive(self):
        try:
            button3 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Эксклюзив')]")))
            logging.info("Кнопка найдена и видна")
            button3.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/videoreports/?isExclusive=1', "Не верный урл кнопки эксклюз"
            return button3
        except TimeoutException:
            return None

    def back(self):
        try:
            back = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Весь спорт')]")))
            logging.info("Кнопка найдена и видна")
            back.click()
            return back
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

    def story(self):
        try:
            story = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Сюжеты')]")))
            logging.info("Сюжеты найдены")
            story.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/stories/', "Не правильный урл сюжета"
            self.browser.back()
            return story
        except TimeoutException:
            return None

    def mma(self):
        try:
            mma = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[@class='se-material-filter-menu__item-button '][contains(text(),'Бокс/ММА')]")))
            logging.info("Кнопка ММа найдена")
            mma.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/martial/videoreports/', "Не правильный урл ММА"
            return mma
        except TimeoutException:
            return None