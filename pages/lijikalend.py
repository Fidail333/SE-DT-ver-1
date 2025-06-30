from itertools import count

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LijiCelndar:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/skiing/kubok-mira/')
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

    def calend(self):
        calend = self.browser.find_element(By.XPATH,"//a[@class='se-menu-subtop__link'][contains(text(),'Календарь')]")
        calend.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/winter/skiing/kubok-mira/2024-2025/calendar/', "Не правильный календарь"

    def filters(self):
        filters = self.browser.find_element(By.XPATH,"//div[@class='se-page-filters']")

    def sprint(self):
        sprint = self.browser.find_element(By.XPATH,"//div[@class='se-competition-titled-block__content']//div[2]//div[2]//div[2]//div[2]//div[1]//a[1]//div[3]")
        sprint.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/live/skiing/kubok-mira/event-16267/', "Не правильный спринт"
        self.browser.back()

    def myj(self):
        myj = self.browser.find_element(By.XPATH,"//div[contains(text(),'Муж')]")
        myj.click()

    def jen(self):
        jen = self.browser.find_element(By.XPATH,"//div[contains(text(),'Жен')]")
        jen.click()

    def smesh(self):
        smesh = self.browser.find_element(By.XPATH,"//div[contains(text(),'Смеш')]")
        smesh.click()

    def vse(self):
        vse = self.browser.find_element(By.XPATH,"//div[@class='se-buttons-toggle-item'][contains(text(),'Все')]")
        vse.click()

    def etap(self):
        etap = self.browser.find_element(By.XPATH,"//div[@class='se-select__value-container'][contains(text(),'Этап')]")
        etap.click()

    def ryka(self):
        ryka = self.browser.find_element(By.XPATH,"//div[@class='se-page-filter se-page-filter--size-100 se-page-filter--max-size-130']//div[@class='se-select__items']//div[2]")
        ryka.click()

    def kol_vo(self,count):
        kol_vo = self.browser.find_elements(By.XPATH,"//div[@class='sp-calendar__race-name']")
        assert len(kol_vo) == count

    def displ(self):
        displ = self.browser.find_element(By.XPATH,"//div[@class='se-select__value-container'][contains(text(),'Дисциплина')]")
        displ.click()

    def mass(self):
        mass = self.browser.find_element(By.XPATH,"//div[@class='se-page-filter se-page-filter--max-size-150']//div[6]")
        mass.click()