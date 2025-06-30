from itertools import count

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FigurkaEuropa:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/figure-skating/chempionat-evropy/')
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

    def poll(self):
        poll = self.browser.find_element(By.XPATH, "//section[@class='se-titled-block mb_30']")

    def podval(self):
        podval = self.browser.find_element(By.XPATH, '//footer[@class="se-footer"]')

    def photo(self):
        photo = self.browser.find_element(By.XPATH,"//article[@class='se-material se-material--type-with_smaller_photo_top']//a[contains(text(),'От пьедестала с Загитовой до вершины в Эспоо: Анас')]")
        photo.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/figure-skating/chempionat-evropy/photoreports/anastasiya-gubanova-vyigrala-chempionat-evropy-po-figurnomu-kataniyu-v-espoo-foto-2029620/'
        self.browser.back()

    def new_photo(self):
        new_photo = self.browser.find_element(By.XPATH,"//a[contains(text(),'Новые альбомы')]")
        new_photo.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/figure-skating/chempionat-evropy/photoreports/',"Не правильный альбом"
        self.browser.back()

    def rss(self):
        rss = self.browser.find_element(By.XPATH,"//a[contains(text(),'RSS, Телеграм бот, Дзен')]")
        rss.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/company/rss/', "Не правильный рсс"
        self.browser.back()

    def allnews(self):
        allnews = self.browser.find_element(By.XPATH,"//a[@class='se-button se-button--size-middle']")
        allnews.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/figure-skating/chempionat-evropy/news/', "Не правильные все новости"
        self.browser.back()

    def allrewiews(self):
        allrewiews = self.browser.find_element(By.XPATH,"//a[contains(text(),'Больше статей')]")
        allrewiews.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/figure-skating/chempionat-evropy/reviews/', "Не правильные все статьи"
        self.browser.back()

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-menu-subtop__link']")
        dop_menu.click()

    def comand(self):
        comand = self.browser.find_element(By.XPATH,"//div[@class='se-menu-subtop-popup']//div[2]")
        comand.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/winter/figure-skating/chempionat-evropy/2024-2025/teams/', "Не правильные команды"

    def title(self):
        title = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def god(self):
        god = self.browser.find_element(By.XPATH,"//div[@class='se-sport-navigator__season-name']")
        god.click()

    def god_24(self):
        god_24 = self.browser.find_element(By.XPATH,"//div[@class='se-sport-navigator__suggest__option css-1rtjtum-option'][1]")
        god_24.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/winter/figure-skating/chempionat-evropy/2023-2024/teams/', "Не правильный год"

    def strani(self,count):
        strani = self.browser.find_elements(By.XPATH,"//div[@class='sp-competition-command-list__info']")
        assert len(strani) == count





















