from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
from selenium.common.exceptions import NoSuchElementException


class CardPlayer:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.original_window = None

    def open(self):
        self.browser.get('https://www.sport-express.ru/tag/krishtianu-ronaldu-973/')

    def menu(self):
        try:
            menu = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='se-menu-subtop se-menu-subtop--main']")))
            logging.info("меню найдено")
            return menu
        except TimeoutException:
            return None

    def verify_all_elements(self):
        elements = [
            ("//td[contains(text(),'Вид спорта:')]", "вид спорта"),
            ("//td[contains(text(),'Клуб:')]", "клуб"),
            ("//td[contains(text(),'Возраст:')]", "возраст"),
            ("//td[contains(text(),'Рост:')]", "рост"),
            ("//td[normalize-space()='80']","Вес"),
            ("//td[contains(text(),'5 февраля 1985')]", "дата"),
            ("//td[contains(text(),'Португалия')]", "Гражданство"),
            ("//td[contains(text(),'Амплуа:')]","Амплуа"),
            ("//td[contains(text(),'Номер:')]","Номер")
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

    def bio(self):
        try:
            bio = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='se-tags-player-description__text']")))
            logging.info("Био найдено")
            return bio
        except TimeoutException:
            return None

    def click_info(self):
        try:
            click_info = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//u[contains(text(),'Футбол')]")))
            logging.info("Текст футбол найден")
            click_info.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/football/', "Не правильный урл"
            self.browser.back()

            click_info2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//u[contains(text(),'Аль-Наср')]")))
            logging.info("Команда найдена")
            click_info2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/fk-al-nasr-24643/', "Не правильный урл команды"
            self.browser.back()
            return click_info2
        except TimeoutException:
            return None

    def button_click(self):
        try:
            btn = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Все о спортсмене')]")))
            logging.info("Кнопка все о спортсмене найдена")
            btn.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/football/L/player/2283/seasons/2025-2026/', "Не правильный урл все о спортсмене"
            self.browser.back()

            btn2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Биография')]")))
            logging.info("Кнопка бион не найдена")
            btn2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/football/england/reviews/kratkaya-biografiya-krishtianu-ronaldu-detstvo-klubnaya-i-mezhdunarodnaya-karera-lichnaya-zhizn-1946597/',"не правильный урл био"
            self.browser.back()
            return btn2
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

    def next_page(self):
        try:
            next = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[normalize-space()='5']")))
            logging.info("Кнопка страницы 5 найдена")
            next.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/krishtianu-ronaldu-973/page5/', "Не правильный урл страницы"

            next2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Далее')]")))
            logging.info("Кнопка далее найдена")
            next2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/krishtianu-ronaldu-973/page6/', "Не рпавьный урл страницы 6"
            return next2
        except TimeoutException:
            return None