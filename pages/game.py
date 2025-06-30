from itertools import count

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class Game:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/games/')
        sleep(6)
        sleep(3)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[contains(text(),'Тесты')]")

