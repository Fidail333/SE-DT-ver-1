from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FootballMedal:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/olympics/summer/badminton/2016/medals/')
        sleep(6)

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')
        sleep(2)

    def selector(self):
        selector = self.browser.find_element(By.XPATH,"//div[@class='se-select__value-container'][contains(text(),'Бадминтон')]")
        selector.click()

    def voleyball(self):
        voleyball = self.browser.find_element(By.XPATH,"//div[@class='se-grid2col__left']//div[12]")
        voleyball.click()
        sleep(3)
        assert self.browser.current_url == 'https://www.sport-express.ru/olympics/summer/volleyball/2016/medals/', "Не правильный волейбол"

    def selec2(self):
        selec2 = self.browser.find_element(By.XPATH,"//div[@class='se-select__value-container'][contains(text(),'По видам спорта')]")
        selec2.click()

    def po_date(self):
        po_date = self.browser.find_element(By.XPATH,"//div[@class='se-select se-select--1col se-select--selected se-select--size-large se-select--open se-select--theme-bordered']//div[@class='se-select__items']//div[2]")
        po_date.click()
        sleep(2)
        assert self.browser.current_url == 'https://www.sport-express.ru/olympics/summer/2016/medals/21-08-2016/', "Не правильный дни"

    def title(self):
        title = self.browser.find_element(By.XPATH,"//th[@class='se-olympic__subtitle']")

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[@class='se-olympic-page__title']")

    def prov(self):
        prov = self.browser.find_element(By.XPATH,"//tbody/tr[8]/td[5]/span[1]")

