from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class FootballOlimp:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/olympics/summer/football/2016/calendar/')
        sleep(6)

    def menu_nad_logo(self):
        menu_nad_logo = self.browser.find_element(By.XPATH,"//div[@class='se-menu-subtop se-menu-subtop--breadcrumb']")

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[@class='se-olympic-page__title']")

    def bloki(self):
        bloki = self.browser.find_element(By.XPATH,"//section[@class='se-titled-block']")

    def news_click(self):
        news_click = self.browser.find_element(By.XPATH,'''//a[contains(text(),'Неймар: "Это одно из лучших событий в моей жизни"')]''')
        news_click.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/olympics/rio2016/football/news/neymar-eto-odno-iz-luchshih-sobytiy-v-moey-zhizni-1036248/',"Не правильная ссылка новости"

    def proverka_tag(self):
        proverka_tag = self.browser.find_element(By.XPATH,"//p[@class='se-material-page__rubric']//a[contains(text(),'Рио-2016')]")
        self.browser.back()

    def switch(self):
        switch = self.browser.find_element(By.XPATH,"//div[@class='se-olympic-navigation__switcher-item']")
        switch.click()

    def august10(self):
        august10 = self.browser.find_element(By.XPATH,"//a[normalize-space()='10']")
        august10.click()
        sleep(4)
        assert self.browser.current_url == 'https://www.sport-express.ru/olympics/summer/2016/calendar/10-08-2016/', "Не правильная дата"

    def proverka(self):
        proverka = self.browser.find_element(By.XPATH,"//div[contains(text(),'Джош Бинсток / Сэм Шэхтер')]")

    def vid_sport(self):
        vid_sport = self.browser.find_element(By.XPATH,"//div[@class='se-select__value-container'][contains(text(),'Все виды спорта')]")
        vid_sport.click()

    def vid_sport2(self):
        vid_sport2 = self.browser.find_element(By.XPATH,"//div[@class='se-select__item'][contains(text(),'Баскетбол')]")
        vid_sport2.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/olympics/summer/basketball/2016/calendar/', "Не правильный баскет"

    def prov_bask(self):
        prov_bask = self.browser.find_element(By.XPATH,"//div[@class='el-filter__date']")