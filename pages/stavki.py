from itertools import count

from selenium.webdriver.common.by import By
from time import sleep

class Stavki:

    def __init__(self, browser):
        self.browser = browser


    def open(self):
        self.browser.get('https://www.sport-express.ru/stavki-na-sport/')
        sleep(6)

    def mosaik(self):
        self.browser.find_element(By.XPATH,"//div[@class='se-materials-grid-mosaic']")

    def glavn_news(self):
        glavn_news = self.browser.find_element(By.XPATH,"//div[@class='se-mainnews']//section[@class='se-titled-block']")

    def reviews(self):
        reviews = self.browser.find_element(By.XPATH,"//div[contains(text(),'Статьи')]")

    def news(self):
        news = self.browser.find_element(By.XPATH,"//div[@class='se-newsline']//section[@class='se-titled-block']")

    def lideri(self):
        lideri = self.browser.find_element(By.XPATH,"//div[@class='se-statblock-leaders']//section[@class='se-titled-block']")


