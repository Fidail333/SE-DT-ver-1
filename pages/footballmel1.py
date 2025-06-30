from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FootballMel1:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/football/rus_d1/news/')
        sleep(6)

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Мелбет Первая Лига России по футболу - новости')]")

    def block(self):
        block = self.browser.find_element(By.XPATH,"//div[@class='se-material-list-filter__bottom']")

    def foltri(self):
        foltri = self.browser.find_element(By.XPATH,"//div[@class='se-material-filter-menu']")

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")





