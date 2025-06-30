from itertools import count

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FigurkaLednik:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/figure-skating/ice-age/')
        sleep(6)

    def menu_nad_logo(self):
        menu_nad_logo = self.browser.find_element(By.XPATH,"//div[@class='se-menu-subtop se-menu-subtop--breadcrumb']")

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

    def allmaterials(self):
        allmaterials = self.browser.find_element(By.XPATH,"//a[contains(text(),'Все материалы')]")
        allmaterials.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/figure-skating/ice-age/materials/'

    def materials(self):
        materials = self.browser.find_element(By.XPATH,"//div[@class='se-news-list-page__items']")