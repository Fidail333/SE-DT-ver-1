from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class FormylaTrasa:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/autosport/formula1/drivers/hemilton-lyuis-275/')
        sleep(6)

    def menu_nad_logo(self):
        menu_nad_logo = self.browser.find_element(By.XPATH,"//div[@class='se-menu-subtop se-menu-subtop--breadcrumb']")

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//span[contains(text(),'Льюис Хэмилтон')]")

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15036753990722208']")

    def eshe(self):
        eshe = self.browser.find_element(By.XPATH,"//div[@class='se-menu-subtop__link']")
        eshe.click()

    def trassa(self):
        trass = self.browser.find_element(By.XPATH,"//a[contains(text(),'Трассы')]")
        trass.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/autosport/formula1/circuits/',"Не правильная трасса"

    def doroga(self):
        doroga = self.browser.find_element(By.XPATH,"//a[normalize-space()='Circuit de Barcelona-Catalunya']")
        doroga.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/autosport/formula1/circuits/circuit-de-barcelona-catalunya-25/',"Не правильная дорога"
        self.browser.back()

    def usa(self):
        usa = self.browser.find_element(By.XPATH,"//span[contains(text(),'Гран-при США')]")
        usa.click()
        sleep(3)
        assert self.browser.current_url == 'https://www.sport-express.ru/autosport/formula1/calendar/gran-pri-ssha_2025-1159/', "Не правильная США"








