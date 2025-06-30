from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class StoryPage:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.original_window = None


    def open_story(self):
        self.browser.get('https://www.sport-express.ru/stories/')

    def h1_story(self):
        try:
            h1_story = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//h1[contains(text(),"Весь спорт.")]')))
            logging.info("Заголовок найден")
            return h1_story
        except TimeoutException:
            return None

    def baskt(self):
        try:
            basket = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[@class='se-material-filter-menu__item-button '][contains(text(),'Баскетбол')]")))
            logging.info("Баскетбол найдено")
            basket.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/basketball/stories/', "Не правильный урл баскетболла"
            return basket
        except TimeoutException:
            return None


    def next_page(self):
        try:
            next_page = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Показать еще')]")))
            logging.info("Кнопка показать еще найдена")
            next_page.click()
            sleep(3)
            assert self.browser.current_url == 'https://www.sport-express.ru/basketball/stories/page2/', "Не правильная вторая страница"
            return next_page
        except TimeoutException:
            return None