from itertools import count

from selenium.webdriver.common.by import By
from time import sleep

class Podpiska:

    def __init__(self, browser):
        self.browser = browser


    def open(self):
        self.browser.get('https://www.sport-express.ru/company/subscribe/')
        sleep(6)

    def h3(self):
        h3 = self.browser.find_element(By.XPATH,"//h3[contains(text(),'ПОДПИШИТЕСЬ НА ВЕЧЕРНИЙ СПОРТ-ЭКСПРЕСС')]")

    def input(self):
        input = self.browser.find_element(By.XPATH,"//input[@class='subpro_input pro_mustbe']")

    def button(self):
        button = self.browser.find_element(By.XPATH,"//input[@name='bt_save']")

    def brend(self):
        brend = self.browser.find_element(By.XPATH,"//a[@class='se-staticpage-menu-group__row-item'][contains(text(),'Бренд-центр')]")
        brend.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/brend-centr/?showforever', "не правильная страница бренд"

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Бренд-центр «Спорт-Экспресс»')]")

    def text(self):
        text = self.browser.find_element(By.XPATH,"//p[contains(text(),'Download Sport Express logos')]")







