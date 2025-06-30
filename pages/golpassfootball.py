from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class FootbalGolPas:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/football/L/russia/premier/2023-2024/statistics/goalpass/')
        sleep(6)

    def top3(self,count):
        top3 = self.browser.find_elements(By.XPATH,"//div[@class='se19-players-statistics__player se19-player-statistics']")
        assert len(top3) == count

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH, "//div[@id='adfox_15645683733586888']")

    def asist(self):
        self.browser.get('https://www.sport-express.ru/football/L/russia/premier/2023-2024/statistics/cards/')
        sleep(6)

    def proverka1(self):
        proverka1 = self.browser.find_element(By.XPATH,"//a[contains(text(),'Андрей Егорычев')]")
        proverka1.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/L/player/45166/seasons/2024-2025/'
