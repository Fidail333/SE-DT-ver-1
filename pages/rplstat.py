from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class RplStat:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/football/L/russia/premier/2023-2024/statistics/bombardiers/')
        sleep(6)

    def top3(self,count):
        top3 = self.browser.find_elements(By.XPATH,"//div[@class='se19-players-statistics__player se19-player-statistics']")
        assert len(top3) == count

    def tukavin(self):
        tukavin = self.browser.find_element(By.XPATH,"(//a[contains(text(),'Константин Тюкавин')])[1]")
        tukavin.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/L/player/60422/seasons/2024-2025/', "Не правильный тюкавин"
        self.browser.back()

    def ska(self):
        ska = self.browser.find_element(By.XPATH, "//tbody/tr[8]/td[4]/div[1]/a[1]")
        ska.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/L/command/5/', "Не правильная команда"
        self.browser.back()

    def ronaldo(self):
        ronaldo = self.browser.find_element(By.XPATH, "//a[contains(text(),'Роналдо')]")
        ronaldo.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/L/player/76883/seasons/2025-2026/', "Не правильная команда"
        self.browser.back()

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH, "//div[@id='adfox_15645683733586888']")

    def asist(self):
        self.browser.get('https://www.sport-express.ru/football/L/russia/premier/2023-2024/statistics/assistances/')
        sleep(6)

