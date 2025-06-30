from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class TennisBilly:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/tennis/fedcup/')
        sleep(6)

    def reviews(self):
        reviews = self.browser.find_element(By.XPATH,"//div[contains(text(),'Статьи')]")

    def news(self):
        news = self.browser.find_element(By.XPATH,"//div[@class='se-newsline']//section[@class='se-titled-block']")

    def result(self):
        result = self.browser.find_element(By.XPATH,"//a[contains(text(),'Результаты')]")
        result.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tennis/L/federation/', "Не правильные результаты"

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH, "//div[@id='adfox_15645683733586888']")













