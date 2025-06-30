from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MMAboets:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/fighting/mma/ufc/2024/fighters/')
        sleep(6)

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def filtri(self):
        filtri = self.browser.find_element(By.XPATH,"//div[@class='se-page-filters']")

    def viktor(self):
        viktor = self.browser.find_element(By.XPATH,"//a[contains(text(),'Витор Петрино')]")
        viktor.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/vitor-petrino-26104/', "Не Правильный боец"
        self.browser.back()

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")


