from itertools import count

from selenium.webdriver.common.by import By
from time import sleep

class Info:

    def __init__(self, browser):
        self.browser = browser


    def open(self):
        self.browser.get('https://www.sport-express.ru/company/usematerial/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Правовая информация')]")

    def priloj(self):
        priloj = self.browser.find_element(By.XPATH,"//a[contains(text(),'Приложения на iOS и Android')]")
        priloj.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/projects/apps/', "Не правильный урл приложения"

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//h2[contains(text(),'Официальное мобильное приложение «Спорт-Экспресс» ')]")

    def imga(self):
        imga = self.browser.find_element(By.XPATH,"//img[@src='//ss.sport-express.ru/projects/desktop/img/static-apps.jpg']")

