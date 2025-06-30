from itertools import count

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LijiMir:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/skiing/chempionat-mira/')
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

    def click(self):
        click = self.browser.find_element(By.XPATH,"//a[@class='se-menu-subtop__link'][contains(text(),'Новости')]")
        click.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/skiing/news/'

    def material_filtr(self):
        material_filtr = self.browser.find_element(By.XPATH,"//div[@class='se-material-filter__top']")

    def vid(self):
        vid = self.browser.find_element(By.XPATH,"//div[@class='se-material-filter-menu']")

    def knop(self):
        knop = self.browser.find_element(By.XPATH,"//div[@class='se-material-list-filter__bottom']")

    def glavn(self):
        glavn = self.browser.find_element(By.XPATH,"//a[contains(text(),'Главные')]")
        glavn.click()
        sleep(5)
        assert self.browser.current_url == 'https://www.sport-express.ru/skiing/news/?isEditorialChoice=1', "не правильная главная"

    def chital(self):
        chital = self.browser.find_element(By.XPATH,"//a[contains(text(),'Выбор читателей')]")
        chital.click()
        sleep(4)
        assert self.browser.current_url == 'https://www.sport-express.ru/skiing/news/?isHot=1', "Не правильный выбор читателей"

    def exlisv(self):
        exlisv = self.browser.find_element(By.XPATH,"//a[contains(text(),'Эксклюзив')]")
        exlisv.click()
        sleep(4)
        assert self.browser.current_url == 'https://www.sport-express.ru/skiing/news/?isExclusive=1', "Не правильный эксклюзив"

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")

