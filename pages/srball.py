from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging


class SrBall:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.original_window = None

    def open(self):
        self.browser.get('https://www.sport-express.ru/football/L/russia/premier/2023-2024/statistics/estimation/')


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
                EC.visibility_of_element_located(
                    (By.XPATH, "//p[@class='se19-player-statistics__name']//a[contains(text(),'Джон Кордоба')]")))
            logging.info("Игрок найден и виден")
            plr_clc.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/football/L/player/37436/seasons/2024-2025/', "Не правильыный игрок"
            self.browser.back()
            return plr_clc
        except TimeoutException:
            return None

    def how_much_player(self, expected_count=242):
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
                EC.visibility_of_element_located((By.XPATH, "//span[@id='select2-submenu_level_b_4-container']")))
            logging.info("Филтр найден")
            filtri.click()

            filtri2 = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//li[contains(@id, 'goalpass')]")))
            logging.info("Селектор главная найден")
            filtri2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/football/L/russia/premier/2023-2024/statistics/goalpass/', "Не правильная ссылка"
            return filtri2
        except TimeoutException:
            return None



