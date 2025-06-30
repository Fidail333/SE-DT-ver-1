from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select


class TennisRaiting:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.original_window = None

    def open(self):
        self.browser.get('https://www.sport-express.ru/tennis/L/rates/atp/')

    def menu(self):
        try:
            menu = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')))
            logging.info("Меню найдено и видно")
            return menu
        except TimeoutException:
            return None

    def reklama(self):
        try:
            reklama = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='adfox_15645683733586888']")))
            logging.info("Реклама найдена и видна")
            return reklama
        except TimeoutException:
            return None

    def verify_all_elements(self):
        elements = [
            ("//th[contains(text(),'ФАМИЛИЯ')]", "Заголовок 'ФАМИЛИЯ'"),
            ("//th[contains(text(),'МЕСТО')]", "Заголовок МЕСТО"),
            ("//th[contains(text(),'СТРАНА')]", "Страна"),
            ("//th[contains(text(),'ОЧКИ')]", "Очки"),
            ("//td[normalize-space()='15']", "Номер")
        ]

        all_present = True

        for xpath, description in elements:
            try:
                self.browser.find_element(By.XPATH, xpath)
                logging.info(f"{description} - найден")
            except NoSuchElementException:
                logging.error(f"{description} - не найден")
                all_present = False

        return all_present

    def selector(self):
        try:
            select = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//select[@id='champselect']")))
            logging.info("Селектор выбора сезона найден и видим")
            select = Select(select)
            select.select_by_index(1)
            assert self.browser.current_url == 'https://www.sport-express.ru/tennis/L/rates/wta/', "Не правильный урл"
            return select
        except TimeoutException:
            return None

    def how_much(self, expected_count=62):
        try:
            player = self.wait.until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, "//td[@class='left']")))
            actual_count = len(player)
            if actual_count == expected_count:
                logging.info(f"Найдено {actual_count} игроков (ожидалось {expected_count})")
                return True
            else:
                logging.warning(f"Кол-во игроков:{actual_count} (ожидалось {expected_count})")
                return False
        except TimeoutException:
            logging.error("Не удалось загрузить игроков")
            return False








