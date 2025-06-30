from itertools import count

from selenium.webdriver.common.by import By
from time import sleep

class It:

    def __init__(self, browser):
        self.browser = browser


    def open(self):
        self.browser.get('https://www.sport-express.ru/company/it/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'IT деятельность')]")

    def p(self):
        p = self.browser.find_element(By.XPATH,"//p[contains(text(),'АО «Спорт-Экспресс» осуществляет деятельность в об')]")

    def menu_nad_logo(self):
        menu_nad_logo = self.browser.find_element(By.XPATH,"//div[@class='se-menu-subtop se-menu-subtop--breadcrumb']")

    def eshe(self):
        eshe = self.browser.find_element(By.XPATH,"//div[contains(@class,'se-menu-link se-menu-link--type-more')]")
        eshe.click()

    def razgovor(self):
        razgovor = self.browser.find_element(By.XPATH,"//a[contains(text(),'Разговор по пятницам')]")
        razgovor.click()
        sleep(2)
        assert self.browser.current_url == 'https://www.sport-express.ru/fridays/materials/', "Не правильный урл"

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Все материалы')]")

    def knopka(self):
        knopka = self.browser.find_element(By.XPATH,"//a[contains(text(),'Показать еще')]")
        knopka.click()
        sleep(5)

    def material(self,count):
        material = self.browser.find_elements(By.XPATH,"//div[@class='se-news-list-page__item-right']")
        assert len(material) == count
