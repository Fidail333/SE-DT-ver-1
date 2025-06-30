from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging



class Stadion:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.original_window = None

    def open(self):
        self.browser.get('https://www.sport-express.ru/hockey/L/khl/2023-2024/stadiums/')

    def h1(self):
        try:
            h1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//h1[contains(text(),'Стадионы')]")))
            logging.info("Заголовок найден")
            return h1
        except TimeoutException:
            return None

    def click(self):
        try:
            click_stadium = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Арена-2000')]")))
            logging.info("стадион найден и вдиим")
            click_stadium.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/stadium/38/', "Не правильный урл стадиона"
            self.browser.back()
            return click_stadium
        except TimeoutException:
            return None

    def stadium(self, expected_count=234):
        try:
            player = self.wait.until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, "//td[@class='se-advanced-table-cell']")))
            actual_count = len(player)
            if actual_count == expected_count:
                logging.info(f"Найдено {actual_count} стадионов (ожидалось {expected_count})")
                return True
            else:
                logging.warning(f"Кол-во стадионов:{actual_count} (ожидалось {expected_count})")
                return False
        except TimeoutException:
            logging.error("Не удалось загрузить стадионов")
            return False


    def click_comand(self):
        try:
            click = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//tbody/tr[7]/td[5]/a[1]")))
            logging.info("Команда найдена")
            click.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/dinamo-moskva-hokkey-520/', "Не правильный урл команды"
            self.browser.back()
            return click
        except TimeoutException:
            return None

    def smi2(self):
        try:
            for _ in range(40):
                try:
                    knopka = self.browser.find_element(By.XPATH,"//div[@id='adfox_159523826122331374']")
                    logging.info("Кнопка с тренером найдена и видна")
                    knopka.click()
                    return knopka
                except:
                    self.browser.execute_script("window.scrollBy(0, 500);")
            logging.info("Кнопка с тренером не найден после прокрутки")
            return None
        except TimeoutException:
            return None

    def click_area(self):
        try:
            click_area = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'ЦСКА Арена')]")))
            logging.info("ЦСКА арена найдена")
            click_area.click()
            self.browser.back()
            return click_area
        except TimeoutException:
            return None

    def season(self):
        try:
            season = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='css-kxyrhr-control']")))
            logging.info("Селектор выбора сезона найден и видим")
            season.click()

            season2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='css-1ez06au-menu']//div[contains(@class, 'css-114a6ms-option') and text()='2020-2021']")))
            logging.info("Сезон найден и видим")
            season2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/khl/2020-2021/stadiums/', "Не правильный урл сезона"
            return season2
        except TimeoutException:
            return None