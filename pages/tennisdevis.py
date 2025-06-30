from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class TennisDevis:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/tennis/davis-cup/')
        sleep(6)

    def reviews(self):
        reviews = self.browser.find_element(By.XPATH,"//div[contains(text(),'Статьи')]")

    def news(self):
        news = self.browser.find_element(By.XPATH,"//div[@class='se-newsline']//section[@class='se-titled-block']")

    def result(self):
        result = self.browser.find_element(By.XPATH,"//a[@class='se-menu-subtop__link'][contains(text(),'Результаты')]")
        result.click()
        sleep(4)
        assert self.browser.current_url == 'https://www.sport-express.ru/tennis/L/davis/', "Не правильный девис"

    def god(self):
        god = self.browser.find_element(By.XPATH,"//select[@class='common_height_26 mb_10'][1]")
        god.click()
        select = Select(god)
        select.select_by_index(2)
        assert self.browser.current_url == 'https://www.sport-express.ru/tennis/L/davis/2023/',"Не правильный год"

    def grupp(self):
        grupp = self.browser.find_element(By.XPATH,"//select[@class='common_height_26 mb_10'][2]")
        grupp.click()
        select = Select(grupp)
        select.select_by_index(4)
        assert self.browser.current_url == 'https://www.sport-express.ru/tennis/L/davis/2023/96/', "Не правильная группа"

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")









