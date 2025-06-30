from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging


class PhotoPage:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.original_window = None

    def open_photo(self):
        self.browser.get('https://www.sport-express.ru/photoreports/')
        sleep(6)

    def h1_photo(self):
        try:
            h1_photo = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//h1[contains(text(),'Весь спорт.')]")))
            logging.info("Заголовок найден")
            return h1_photo
        except TimeoutException:
            return None

    def poll(self):
        try:
            poll = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[@class='se-material-filter-headline__item'][contains(text(),'Опросы')]")))
            logging.info("Опросы найдены")
            poll.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/poll/', "Не правильная ссылка опросов"
            self.browser.back()
            return poll
        except TimeoutException:
            return None

    def fig(self):
        try:
            fig = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(@class,'se-material-filter-menu__item-button')][contains(text(),'Фигурное катание')]")))
            logging.info("Фигурное катание найдено")
            fig.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/figure-skating/photoreports/', "Не правильный урл фигурки"
            return fig
        except TimeoutException:
            return None

    def reviews(self,expected_count=30):
        try:
            reviews = self.wait.until(
                EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='se-photo-list-page__item']")))
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