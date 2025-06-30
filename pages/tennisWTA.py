from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class TennisWTA:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/tennis/wta/')
        sleep(6)

    def reviews(self):
        reviews = self.browser.find_element(By.XPATH,"//div[contains(text(),'Статьи')]")

    def news(self):
        news = self.browser.find_element(By.XPATH,"//div[@class='se-newsline']//section[@class='se-titled-block']")

    def tournir(self):
        tournir = self.browser.find_element(By.XPATH,"//a[contains(text(),'Турниры')]")
        tournir.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tennis/L/wta/', "Не правильный ВТА"












