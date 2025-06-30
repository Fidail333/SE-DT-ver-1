from itertools import count

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class TennisAtp:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/tennis/atp/')
        sleep(6)

    def news(self):
        news = self.browser.find_element(By.XPATH,"//div[@class='se-newsline']//section[@class='se-titled-block']")

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")

    def rait(self):
        rait = self.browser.find_element(By.XPATH,"//a[@class='se-menu-subtop__link'][contains(text(),'Рейтинг')]")
        rait.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tennis/L/rates/atp/', "Не правильный рейтинг теннис"

    def spisok(self):
        spisok = self.browser.find_element(By.XPATH,"//td[contains(text(),'Филс Артур')]")

    def vibor(self):
        vibor = self.browser.find_element(By.XPATH,"//select[@id='champselect']")
        vibor.click()
        select = Select(vibor)
        select.select_by_index(1)
        assert self.browser.current_url == 'https://www.sport-express.ru/tennis/L/rates/wta/', "Не правильный ВТА"




