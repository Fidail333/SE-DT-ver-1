from itertools import count

from selenium.webdriver.common.by import By
from time import sleep

class Contakt:

    def __init__(self, browser):
        self.browser = browser


    def open(self):
        self.browser.get('https://www.sport-express.ru/company/contacts/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Контактная информация')]")

    def tel(self):
        tel = self.browser.find_element(By.XPATH,"//p[normalize-space()='+7 (495) 540-70-10']")

    def email(self):
        email = self.browser.find_element(By.XPATH,"//a[normalize-space()='feedback@sport-express.ru']")

    def podpiska(self):
        podpiska = self.browser.find_element(By.XPATH,"//a[contains(text(),'Подписка на газету')]")
        podpiska.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/subscribe/', "Не правльная ссылка подписки"

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"(//h1[@class='se19-staticpage-h1'])[1]")

    def oformit(self):
        oformit = self.browser.find_element(By.XPATH,"(//a[contains(text(),'Оформить подписку')])[1]")
        oformit.click()
        assert self.browser.current_url == 'https://podpiska.pochta.ru/search?query=%D1%81%D0%BF%D0%BE%D1%80%D1%82-%D1%8D%D0%BA%D1%81%D0%BF%D1%80%D0%B5%D1%81%D1%81', "Не правильная ссылка газеты"

