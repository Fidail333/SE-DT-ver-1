from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class EuroHockey:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/hockey/L/europe/2023-2024/calendar/')
        sleep(6)

    def menu_nad_logo(self):
        menu_nad_logo = self.browser.find_element(By.XPATH,"//div[@class='se-menu-subtop se-menu-subtop--breadcrumb']")

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Еврохоккейтур. Календарь/Результаты')]")

    def filtri(self):
        filtri = self.browser.find_element(By.XPATH,"//div[@class='se-page-filters se-page-filters--overflow-overlay']")

    def perexod(self):
        perexod = self.browser.find_element(By.XPATH,"//div[@class='sp-competition-calendar']//div[1]//div[1]//div[1]//div[1]//div[5]//a[1]//div[1]//div[1]//div[3]")
        perexod.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/matchcenter/116320/', "Не правлиный урл"

    def book(self):
        book = self.browser.find_element(By.XPATH,"//div[@class='sp-competition-calendar__bookie']")


