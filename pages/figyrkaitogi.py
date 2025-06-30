from itertools import count

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FigurkaItogi:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/live/figure-skating/chempionat-rossii/event-16113/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def knopki(self):
        knopki = self.browser.find_element(By.XPATH,"//div[@class='sp-matchcenter-event-submenu']")

    def vkladki(self):
        vkladki = self.browser.find_element(By.XPATH,"//div[@class='sp-matchcenter-event-personal-results__stages']")

    def final(self):
        final = self.browser.find_element(By.XPATH,"//h2[contains(text(),'Елизавета Худайбердиева / Егор Базин')]")
        final.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/elizaveta-hudayberdyeva-egor-bazin-20784/', "Не правильный финалист"
        self.browser.back()

    def sportsmn(self):
        sportsmn = self.browser.find_element(By.XPATH,"//a[contains(text(),'Варвара Жданова / Тимур Бабаев-Смирнов')]")
        sportsmn.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/varvara-zhdanova-timur-babaev-smirnov-24855/', "Не правильный спортсмен"
        self.browser.back()

    def book(self):
        book = self.browser.find_element(By.XPATH,"//div[@class='se-bookie-badge-with-adv']")

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")

    def tegi(self):
        tegi = self.browser.find_element(By.XPATH,"//div[@class='se-tagblock__items']")












