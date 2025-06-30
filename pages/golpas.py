from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging


class GolAndPass:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.original_window = None

    def open(self):
        self.browser.get('https://www.sport-express.ru/football/L/russia/first/2023-2024/statistics/goalpass/')

    def menu_nadlogo(self):
        try:
            menu = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')))
            logging.info("меню найдено и видимо")
            return menu
        except TimeoutException:
            return None

    def player(self, expected_count=3):
        try:
            player = self.wait.until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, "//div[@class='se19-players-statistics__player se19-player-statistics']")))
            actual_count = len(player)
            if actual_count == expected_count:
                logging.info(f"Найдено {actual_count} бомбардиров (ожидалось {expected_count})")
                return True
            else:
                logging.warning(f"Кол-во бомбардиров:{actual_count} (ожидалось {expected_count})")
                return False
        except TimeoutException:
            logging.error("Не удалось загрузить бомбардиров")
            return False

    def player_click(self):
        try:
            plr_clc = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//p[@class='se19-player-statistics__name']//a[contains(text(),'Александр Ломакин')]")))
            logging.info("Игрок найден и виден")
            plr_clc.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/football/L/player/33703/seasons/2024-2025/', "Не правильыный игрок"
            self.browser.back()
            return plr_clc
        except TimeoutException:
            return None

    def how_much_player(self, expected_count=323):
        try:
            players = self.wait.until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, "//td[@class='se19-table-statistics__td se19-table-statistics__td--name']")))
            actual_count = len(players)
            if actual_count == expected_count:
                logging.info(f"Найдено {actual_count} бомбардиров (ожидалось {expected_count})")
                return True
            else:
                logging.warning(f"Кол-во бомбардиров:{actual_count} (ожидалось {expected_count})")
                return False
        except TimeoutException:
            logging.error("Не удалось загрузить бомбардиров")
            return False

    def filti(self):
        try:
            filtri = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//span[@id='select2-submenu_level_b_3-container']")))
            logging.info("Филтр найден")
            filtri.click()

            filtri2 = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//li[contains(@id, 'select2-submenu_level_b_3-result-') and text()='Календарь']")))
            logging.info("Селектор главная найден")
            filtri2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/football/L/russia/first/2023-2024/calendar/tours/', "Не правильная ссылка"
            return filtri2
        except TimeoutException:
            return None







