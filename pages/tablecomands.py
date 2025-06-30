from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class TableComands:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.original_window = None

    def open(self):
        self.browser.get('https://www.sport-express.ru/football/L/russia/premier/2024-2025/')

    def h1(self):
        try:
            h1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//h1[contains(text(),'Россия. Премьер-лига 2024-2025, турнирные таблицы')]")))
            logging.info("Загловок найден")
            return h1
        except TimeoutException:
            return None

    def data_table(self):
        try:
            table1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//span[@id='select2-submenu_level_b_2-container']")))
            logging.info("Кнопка даты таблиц найдена")
            table1.click()

            table2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//li[contains(@class, 'select2-results__option') and text()='2023-2024']")))
            logging.info("Календарь найден и виден")
            table2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/football/L/russia/premier/2023-2024/', "Не правильная дата"
            return table2
        except TimeoutException:
            return None

    def loko(self):
        try:
            loko = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='se19-flex-nowrap align-items-center']//span[@class='m_all link-underline']//a[contains(text(),'Локомотив')]")))
            logging.info("Команда найдена и видна")
            loko.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/football/L/command/11/', "Не правильная команда"
            self.browser.back()
            return loko
        except TimeoutException:
            return None

    def legend(self):
        try:
            legend = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'-  Зона вылета')]")))
            logging.info("Легенда найдена")
            return legend
        except TimeoutException:
            return None