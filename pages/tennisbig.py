from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class TennisBig:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/tennis/grand-slam/')
        sleep(6)

    def reviews(self):
        reviews = self.browser.find_element(By.XPATH,"//div[contains(text(),'Статьи')]")

    def news(self):
        news = self.browser.find_element(By.XPATH,"//div[@class='se-newsline']//section[@class='se-titled-block']")

    def plitka(self):
        plitka = self.browser.find_element(By.XPATH,"//div[@class='se-materials-grid-mosaic']")

    def auopen(self):
        auopen = self.browser.find_element(By.XPATH,"//a[normalize-space()='Australian Open']")
        auopen.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tennis/L/big/ausopen/', "Не правильный турнир"

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[normalize-space()='Australian Open']")

    def book(self):
        book = self.browser.find_element(By.XPATH,"//h1[normalize-space()='Australian Open']")

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")









