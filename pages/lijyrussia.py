from itertools import count

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LijiRussia:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/skiing/chempionat-rossii/')
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

    def rss(self):
        rss = self.browser.find_element(By.XPATH,"//a[@class='se-button se-button--inline se-button--size-middle']")
        rss.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/company/rss/', "Не правильный рсс"
        self.browser.back()

    def allreviews(self):
        allreviews = self.browser.find_element(By.XPATH,"//a[contains(text(),'Больше статей')]")
        allreviews.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/skiing/chempionat-rossii/reviews/', "Не правлиьная кнопка"
        self.browser.back()

    def click(self):
        click = self.browser.find_element(By.XPATH,"//a[@class='se-menu-subtop__link'][contains(text(),'Новости')]")
        click.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/skiing/chempionat-rossii/news/', "Не правильный клик"

    def filtri(self):
        filtri = self.browser.find_element(By.XPATH,"//div[@class='se-material-list-filter__bottom']")

