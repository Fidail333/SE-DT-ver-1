from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class FormylaCalendar:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/autosport/formula1/results/?season=2024')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//span[contains(text(),'Результаты')]")

    def menu_nad_logo(self):
        menu_nad_logo = self.browser.find_element(By.XPATH,"//div[@class='se-menu-subtop se-menu-subtop--breadcrumb']")

    def peres(self):
        peres = self.browser.find_element(By.XPATH,"//a[contains(text(),'Серхио Перес')]")
        peres.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/autosport/formula1/drivers/peres-serhio-619/', "не правильный перец"
        self.browser.back()

    def race(self):
        race = self.browser.find_element(By.XPATH,"//a[contains(text(),'Календарь гонок')]")
        race.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/autosport/formula1/calendar/',"не правильный календарь гонок"

    def text(self):
        text = self.browser.find_element(By.XPATH,"//span[contains(text(),'Календарь гонок')]")

    def belgia(self):
        belgia = self.browser.find_element(By.XPATH,"//span[contains(text(),'Гран-при Бельгии')]")
        belgia.click()
        sleep(4)
        assert self.browser.current_url == 'https://www.sport-express.ru/autosport/formula1/calendar/gran-pri-belgii_2025-1153/', "Не правильная бельгия"
        self.browser.back()





