from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FigurkaKalend:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/figure-skating/chempionat-rossii/')
        sleep(6)

    def menu_nad_logo(self):
        menu_nad_logo = self.browser.find_element(By.XPATH,"//div[@class='se-menu-subtop se-menu-subtop--breadcrumb']")

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

    def calendar(self):
        calendar = self.browser.find_element(By.XPATH,"//a[contains(text(),'Календарь')]")
        calendar.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/winter/figure-skating/chempionat-rossii/2024-2025/calendar/', "Не правильный каледнраь"

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def tag(self):
        tag = self.browser.find_element(By.XPATH,"//div[contains(text(),'Популярные теги')]")

    def book(self):
        book = self.browser.find_element(By.XPATH,"//div[@class='se-bookie-badge-with-adv']")

    def match(self):
        match = self.browser.find_element(By.XPATH,"//div[contains(text(),'Пары, короткая программа')]")
        match.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/live/figure-skating/chempionat-rossii/event-16438/',"Не правльная игра"








