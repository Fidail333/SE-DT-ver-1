from itertools import count

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class TrenerKhl:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/hockey/L/khl/2023-2024/trainers/')
        sleep(6)

    def menu_nad_logo(self):
        menu_nad_logo = self.browser.find_element(By.XPATH,"//div[@class='se-menu-subtop se-menu-subtop--breadcrumb']")

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Тренеры')]")

    def roten(self):
        roten = self.browser.find_element(By.XPATH,"(//img[@title='Ротенберг Роман'])[1]")
        roten.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/trainer/454/'
        self.browser.back()

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")

    def podval(self):
        podval = self.browser.find_element(By.XPATH,"//footer[@class='se-footer']")
