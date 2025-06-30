from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasketVtb:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/basketball/vtb-league/')
        sleep(6)

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")

    def reviews(self):
        reviews = self.browser.find_element(By.XPATH, "//div[contains(text(),'Статьи')]")

    def news(self):
        news = self.browser.find_element(By.XPATH, "//div[@class='se-newsline']//section[@class='se-titled-block']")

    def podval(self):
        podval = self.browser.find_element(By.XPATH,"//footer[@class='se-footer']")

    def table(self):
        table = self.browser.find_element(By.XPATH,"//a[contains(text(),'Таблицы')]")
        table.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/basketball/L/men/vtb/2024-2025/', "Не правильные таблицы"

    def champ(self):
        champ = self.browser.find_element(By.XPATH,"//h3[contains(text(),'Регулярный чемпионат')]")

    def comand(self):
        comand = self.browser.find_element(By.XPATH,"//td[contains(text(),'Пари НН')]")













