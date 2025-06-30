from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class NewsPhoto:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 15)
        self.original_window = None


    def open_photo_news(self):
        self.browser.get('https://www.sport-express.ru/football/rfpl/photoreports/spartak-proigral-fakelu-v-matche-rpl-v-luzhnikah-foto-igry-10-marta-2024-2188299/')

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
                EC.visibility_of_element_located((By.XPATH,"//h1[contains(text(),'Утешение Абаскаля и тату на сердце фаната: «Факел»')]")))
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

    def tags(self):
        try:
            tags = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'ФК Спартак (Москва)')]")))
            logging.info("Тег найден!")
            tags.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/spartak-futbol-514/', "Тег спартака не правильный"
            self.browser.back()
            return tags
        except TimeoutException:
            return None

    def click_share(self):
        try:
            click_share = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='se-shareblock se-material-user-actions-aside__share se-shareblock--popup-rows se-shareblock--popup']")))
            logging.info("Кнопка поделиться найдена")
            click_share.click()
            return click_share
        except TimeoutException:
            return None

    def sociaty(self,expected_count=5):
        try:
            sociaty = self.wait.until(
                EC.visibility_of_all_elements_located((By.XPATH,"//button[@class='react-share__ShareButton']")))
            actual_count = len(sociaty)
            if actual_count == expected_count:
                logging.info(f"Найдено {actual_count} статей (ожидалось {expected_count})")
                return True
            else:
                logging.warning(f"Кол-во статей:{actual_count} (ожидалось {expected_count})")
                return False
        except TimeoutException:
            logging.error("Не удалось загрузить список статей")
            return False

    def stat(self):
        try:
            stat = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Статистика')]")))
            logging.info("Статитстика найдена")
            stat.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/football/L/russia/premier/2025-2026/statistics/bombardiers/', "Не правильная статистика"
            return stat
        except TimeoutException:
            return None






