from itertools import count

from selenium.webdriver.common.by import By
from time import sleep

class Raiting:

    def __init__(self, browser):
        self.browser = browser


    def open(self):
        self.browser.get('https://www.sport-express.ru/rating-bookmakerov/news/reyting-bukmekerov-1989757/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Рейтинг букмекеров')]")

    def nadej(self):
        nadej = self.browser.find_element(By.XPATH,"//div[@class='se-bookies-ratings__filter']")

    def spisok(self):
        spisok = self.browser.find_element(By.XPATH,"//div[@class='se-bookies-ratings__content']")

    def olimp(self):
        olimp =self.browser.find_element(By.XPATH,"//a[normalize-space()='OLIMPBET']")
        olimp.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/rating-bookmakerov/news/olimp-1989736/', "Не правильный букмекер"
        self.browser.back()

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")

    def knopka(self):
        knopka = self.browser.find_element(By.XPATH,"//div[@class='se-button se-button--size-big']")
        knopka.click()

    def proverka(self,count):
        proverka = self.browser.find_elements(By.XPATH,"//div[@class='se-bookies-ratings__table-td se-bookies-ratings__table-td--col-company']")
        assert len(proverka) == count

    def polojenie(self):
        polojenie = self.browser.find_element(By.XPATH,"//div[contains(text(),'Положение команд')]")

    def eshe(self):
        eshe = self.browser.find_element(By.XPATH,"//div[@class='se-menu-link se-menu-link--type-more ']")
        eshe.click()

    def golshak(self):
        golshak = self.browser.find_element(By.XPATH,"//a[contains(text(),'Голышак вспоминает')]")
        golshak.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/golyshak-vspominaet/', "Не правильный урл"

    def reviews(self):
        reviews = self.browser.find_element(By.XPATH,"//div[contains(text(),'Статьи')]")






