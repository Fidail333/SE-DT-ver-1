from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class TexnoRviews:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/cybersport/reviews/')
        sleep(6)

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, "//div[@class='se-menu-subtop se-menu-subtop--breadcrumb']")

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Техно. Статьи')]")

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")

    def vid_mat(self):
        vid_mat = self.browser.find_element(By.XPATH,"//div[@class='se-material-filter__top']")

    def vid_sport(self):
        vid_sport = self.browser.find_element(By.XPATH,"//div[@class='se-material-filter-menu']")

    def knopki(self):
        knopki = self.browser.find_element(By.XPATH,"//div[@class='se-material-list-filter__bottom']")



















