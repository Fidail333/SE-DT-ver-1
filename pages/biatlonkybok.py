from itertools import count

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BiatlonKybok:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/biathlon/kubok-mira/')
        sleep(6)

    def menu_nad_logo(self):
        menu_nad_logo = self.browser.find_element(By.XPATH, "//div[@class='se-menu-subtop se-menu-subtop--breadcrumb']")

    def plitka_glavn(self):
        plitka_glavn = self.browser.find_element(By.XPATH, "//div[@class='se-materials-grid-mosaic']")

    def glavn_news(self):
        glavn_news = self.browser.find_element(By.XPATH,'''//div[@class='se-mainnews']//section[@class="se-titled-block"]''')

    def news(self):
        news = self.browser.find_element(By.XPATH, '''//div[@class='se-newsline']//section[@class="se-titled-block"]''')

    def reviews(self):
        reviews = self.browser.find_element(By.XPATH, "//div[contains(text(),'Статьи')]")

    def podval(self):
        podval = self.browser.find_element(By.XPATH, '//footer[@class="se-footer"]')

    def obsh_za4(self):
        obsh_za4 = self.browser.find_element(By.XPATH,"//a[contains(text(),'Общий зачет')]")
        obsh_za4.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/winter/biathlon/kubok-mira/2024-2025/standing/men/', "Не правильный общий зачет"

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='se-competition-titled-block__title']")

    def nation(self):
        nation = self.browser.find_element(By.XPATH,"//a[contains(text(),'Кубок наций')]")
        nation.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/winter/biathlon/kubok-mira/2024-2025/nationscup/men/', "Не правильный нация"

    def strani(self,count):
        strani = self.browser.find_elements(By.XPATH,"//a[@class='se-router-link']")
        assert len(strani) == count

    def usa(self):
        usa = self.browser.find_element(By.XPATH,"//a[contains(text(),'США')]")
        usa.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/sbornaya-soedinennyh-shtatov-ameriki-biathlon-20276/', "Не правильный США"
        self.browser.back()

    def knopa(self):
        knopa = self.browser.find_element(By.XPATH,"//div[@class='se-view-toggle__view']")
        knopa.click()
        sleep(3)

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")
