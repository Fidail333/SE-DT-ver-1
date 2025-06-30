from itertools import count

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class HocckeyStat:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/hockey/world/')
        sleep(6)

    def menu_nad_logo(self):
        menu_nad_logo = self.browser.find_element(By.XPATH,"//div[@class='se-menu-subtop se-menu-subtop--breadcrumb']")

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

    def poll(self):
        poll = self.browser.find_element(By.XPATH, "//section[@class='se-titled-block mb_30']")

    def podval(self):
        podval = self.browser.find_element(By.XPATH, '//footer[@class="se-footer"]')

    def stat(self):
        stat = self.browser.find_element(By.XPATH,"//a[contains(text(),'Статистика')]")
        stat.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/world/2024/statistic/', "Не правильная статистика"

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Чемпионат мира. Статистика. Лидеры')]")

    def kevin(self):
        kevin = self.browser.find_element(By.XPATH,"(//img[@title='Фиала Кевин'])[1]")
        kevin.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/kevin-fiala-13780/'
        self.browser.back()

    def comandni(self):
        comandni = self.browser.find_element(By.XPATH,"//a[contains(text(),'Командная')]")
        comandni.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/world/2024/statistic/teams/', "Не правильная командная"

    def playoff(self):
        playoff = self.browser.find_element(By.XPATH,"//div[@class='sp-playoff-table']//div[@class='se-titled-block se-titled-block--bg-white']")

