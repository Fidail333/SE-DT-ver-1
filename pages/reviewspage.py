from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging


class ReviewsPage:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.original_window = None

    def open(self):
        self.browser.get('https://www.sport-express.ru/reviews/')
        sleep(6)

    def h1_rev(self):
        try:
            h1_rev = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//h1[contains(text(),"Весь спорт.")]')))
            logging.info("Заголовок найден")
            return h1_rev
        except TimeoutException:
            return None

    def button_main(self):
        try:
            button1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//a[contains(text(),"Главные")]')))
            logging.info("Кнопка найдена и видна")
            button1.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/reviews/?isEditorialChoice=1', "Неверный урл Главные кнопки"
            return button1
        except TimeoutException:
            return None

    def button_readers(self):
        try:
            button2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//a[contains(text(),"Выбор читателей")]')))
            logging.info("Кнопка найдена и видна")
            button2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/reviews/?isHot=1', "Не верный урл Выбор читателей"
            return button2
        except TimeoutException:
            return None

    def button_exclusive(self):
        try:
            button3 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Эксклюзив')]")))
            logging.info("Кнопка найдена и видна")
            button3.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/reviews/?isExclusive=1', "Не верный урл кнопки эксклюз"
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

    def photo_vid(self):
        try:
            photo_vid = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[@class='se-material-filter-headline__item'][contains(text(),'Фото')]")))
            logging.info("Кнопка Фото найдена и видна")
            photo_vid.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/photoreports/', "Не правильная кнопка фото"
            self.browser.back()
            return photo_vid
        except TimeoutException:
            return None

    def hockey_button(self):
        try:
            hockey_button = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'''//a[contains(@class,'se-material-filter-menu__item-button')][contains(text(),"Хоккей")]''')))
            logging.info("Кнопка найдена и видна")
            hockey_button.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/hockey/reviews/', "Не правильный урл хоккея"
            return hockey_button
        except TimeoutException:
            return None

    def reviews(self,expected_count=30):
        try:
            reviews = self.wait.until(
                EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='se-press-list-page__item']")))
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


