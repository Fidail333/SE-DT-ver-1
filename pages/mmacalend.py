from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MMAcalend:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/fighting/mma/ufc/2024/calendar/')
        sleep(6)

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def filtr1(self):
        filtr1 = self.browser.find_element(By.CSS_SELECTOR,".se-sport-navigator__competition")
        filtr1.click()

    def aca(self):
        aca = self.browser.find_element(By.CSS_SELECTOR,"#react-select-competitions-option-0-4")
        aca.click()
        sleep(3)
        assert self.browser.current_url == 'https://www.sport-express.ru/fighting/mma/aca/2025/calendar/', "Не правильная аса"

    def ves(self):
        ves = self.browser.find_element(By.XPATH,"//div[@class='se-select__value-container'][contains(text(),'Вес')]")
        ves.click()

    def hightves(self):
        hightves = self.browser.find_element(By.XPATH,"//div[@class='se-select__item'][contains(text(),'Тяжелый вес')]")
        hightves.click()





