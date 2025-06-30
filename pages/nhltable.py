from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class NhlTable:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/hockey/nhl/')
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

    def table(self):
        table = self.browser.find_element(By.XPATH,"//a[contains(text(),'Таблицы')]")
        table.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/nhl/2024-2025/', "Не правильные таблицы"

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'НХЛ. Турнирная таблица')]")

    def conference(self):
        conference = self.browser.find_element(By.XPATH,"//a[contains(text(),'Конференции')]")
        conference.click()
        sleep(3)
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/nhl/2024-2025/?type=conference', "Не правильная конференция"

    def ottava(self):
        ottava = self.browser.find_element(By.XPATH,"(//img[@title='Оттава'])[1]")
        ottava.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/ottava-senatorz-1413/', "Не правильная команда"