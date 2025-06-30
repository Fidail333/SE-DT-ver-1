from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class FootballMc:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/live/football/')
        sleep(6)

    def menu_nad_logo(self):
        menu_nad_logo = self.browser.find_element(By.XPATH,"//div[@class='se-menu-subtop se-menu-subtop--breadcrumb']")

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_150367506386015242']")

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def vidmaterial(self):
        vidmaterial = self.browser.find_element(By.XPATH,"//div[@class='swiper-wrapper']")

    def date(self):
        date = self.browser.find_element(By.XPATH,"//div[@data-component='matchcenter-filter']")

    def sport_list(self):
        sport_list = self.browser.find_element(By.XPATH,"//div[@class='se-matchcenter-sports-list']")



