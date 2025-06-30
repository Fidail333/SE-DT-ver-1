from itertools import count

from selenium.webdriver.common.by import By
from time import sleep

class Rss:

    def __init__(self, browser):
        self.browser = browser


    def open(self):
        self.browser.get('https://www.sport-express.ru/company/rss/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"(//h1[@class='se19-staticpage-h1'])[1]")

    def rss(self,count):
        rss = self.browser.find_elements(By.XPATH,"//li[@class='se19-triple-arrow mb_20']")
        assert len(rss) == count

    def foot_rss(self):
        foot_rss = self.browser.find_element(By.XPATH,"//a[contains(text(),'RSS футбол')]")
        foot_rss.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/services/materials/news/football/se/', "Не правильный переход по РСС"
        self.browser.back()

    def proverka(self):
        proverka = self.browser.find_element(By.XPATH,"//a[@class='se-staticpage-menu-group__row-item'][contains(text(),'Проверка фактов')]")
        proverka.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/company/checkfacts/', "Не правильная проверка фактов"

    def zag(self):
        zag = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Проверка фактов')]")





