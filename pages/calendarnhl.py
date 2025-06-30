from itertools import count

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class CalendarNhl:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/hockey/nhl/')
        sleep(6)

    def tablo(self):
        tablo = self.browser.find_element(By.XPATH,"//div[@class='se-translation-scoreboard__events']")

    def plitka_glavn(self):
        plitka_glavn = self.browser.find_element(By.XPATH, "//div[@class='se-materials-grid-mosaic']")

    def glavn_news(self):
        glavn_news = self.browser.find_element(By.XPATH,'''//div[@class='se-mainnews']//section[@class="se-titled-block"]''')

    def news(self):
        news = self.browser.find_element(By.XPATH, '''//div[@class='se-newsline']//section[@class="se-titled-block"]''')

    def video(self):
        video = self.browser.find_element(By.XPATH, "//div[@class='se-video-block']")

    def reviews(self):
        reviews = self.browser.find_element(By.XPATH, "//div[contains(text(),'Статьи')]")

    def podval(self):
        podval = self.browser.find_element(By.XPATH, '//footer[@class="se-footer"]')

    def calend(self):
        calend = self.browser.find_element(By.XPATH,"//a[@class='se-menu-subtop__link'][contains(text(),'Календарь')]")
        calend.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/nhl/2024-2025/calendar/',"Не правильный календарь"

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'НХЛ. Календарь/Результаты')]")

    def book(self):
        book = self.browser.find_element(By.XPATH,"//div[@class='sp-competition-calendar__bookie']")

    def bookes(self):
        bookes = self.browser.find_element(By.XPATH,"//div[@class='sp-competition-calendar-match__extra-bookies']")

    def tables(self):
        tables = self.browser.find_element(By.XPATH,"//div[@class='se-titled-block se-titled-block--bg-white']")
