from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class LifeStyle:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/zozh/food/')
        sleep(6)

    def img(self):
        img = self.browser.find_element(By.XPATH,"//div[@class='se-brandedbuttons__item']//img")

    def swipe(self,count):
        swipe = self.browser.find_elements(By.XPATH,"//div[@class='swiper-wrapper']")
        assert len(swipe) == count #4

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH, "//div[@id='adfox_15645683733586888']")

    def news(self):
        news = self.browser.find_element(By.XPATH,"//div[@class='ls-top-news__items']")

    def eshe_news(self):
        eshe_news = self.browser.find_element(By.XPATH,"//div[@class='ls-button ls-button--color-white ls-top-news__more-button']")
        eshe_news.click()

    def proverka_news(self,count):
        proverka_news = self.browser.find_elements(By.XPATH,"//div[@class='ls-top-news__item-title']")
        assert len(proverka_news) == count

    def all_news(self):
        all_news = self.browser.find_element(By.XPATH,"//a[@class='ls-button ls-button--color-color'][contains(text(),'Все новости')]")
        all_news.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/zozh/food/news/', "Не правильные все новости"
        self.browser.back()

    def reviews(self):
        reviews = self.browser.find_element(By.XPATH,"//div[@class='ls-main-articles__top']")

    def eshe_reviews(self):
        eshe_reviews = self.browser.find_element(By.XPATH,"//div[@class='ls-button ls-button--color-white ls-main-articles__more-button']")
        eshe_reviews.click()

    def proverka_reviews(self,count):
        proverka_reviews = self.browser.find_elements(By.XPATH,"//div[@class='ls-main-articles__other']")
        assert len(proverka_reviews) == count

    def all_reviews(self):
        all_reviews = self.browser.find_element(By.XPATH,"//a[contains(text(),'Больше статей')]")
        all_reviews.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/zozh/reviews/', "Не правильный все статьи"
        self.browser.back()

    def vopros(self):
        vopros = self.browser.find_element(By.XPATH,"//div[@class='ls-qa-list__items']")

    def popylar(self):
        popylar = self.browser.find_element(By.XPATH,"//div[@class='ls-best-materials-main-page__items ls-best-materials-main-page__items--top']")

    def expert(self):
        expert = self.browser.find_element(By.XPATH,"//div[@class='ls-experts__content']")

    def podval(self):
        podval = self.browser.find_element(By.XPATH,"//div[@class='se-center-wrapper']")

    def recept(self):
        recept = self.browser.find_element(By.XPATH,"//div[@class='ls-mainpage__rubrics ls-mainpage__rubrics--top']//div//a[@class='ls-rubric-menu-item ls-rubric-menu-item--sub'][contains(text(),'Рецепты')]")
        recept.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/recepty-24608/', "Не правильные рецепты"

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Рецепты')]")

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//h2[contains(text(),'Все материалы')]")












