from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class FormylaKostryktor:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/autosport/formula1/calendar/')
        sleep(6)

    def menu_nad_logo(self):
        menu_nad_logo = self.browser.find_element(By.XPATH,"//div[@class='se-menu-subtop se-menu-subtop--breadcrumb']")

    def kubok(self):
        kubok = self.browser.find_element(By.XPATH,"//a[contains(text(),'Кубок конструкторов')]")
        kubok.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/autosport/formula1/results/constructor/', "констуркторы не правильный"

    def text(self):
        text = self.browser.find_element(By.XPATH,"//span[contains(text(),'Результаты')]")










