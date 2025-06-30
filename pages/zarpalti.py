from itertools import count

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class Zarplati:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/video/den-s-alekseem-shevchenko/materials/')
        sleep(6)

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'День с Алексеем Шевченко. Все материалы')]")

    def spisok(self,count):
        spisok = self.browser.find_elements(By.XPATH,"//div[@class='se-news-list-page__item-right']")
        assert len(spisok) == count

    def knopka(self):
        knopka = self.browser.find_element(By.XPATH,"//a[contains(text(),'Показать еще')]")
        knopka.click()
        sleep(5)
        assert self.browser.current_url == 'https://www.sport-express.ru/video/den-s-alekseem-shevchenko/materials/page2/', "Не прожалась кнопка"

    def zp(self):
        zp = self.browser.find_element(By.XPATH,"//a[@class='se-burger-menu__link'][contains(text(),'Зарплаты КХЛ')]")
        self.browser.get('https://www.sport-express.ru/hockey/khl/money/2024-2025/')
        sleep(6)
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/khl/money/2024-2025/', "Не правлиьный урл"

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//h1[@class='se-player-salaries-main-page__title']")

    def filtri(self):
        filtri = self.browser.find_element(By.XPATH,"//div[@class='se-filters-salaries']")

    def years(self):
        years = self.browser.find_element(By.XPATH,"//body/div[@class='se-player-salaries-layout']/main[@class='se-player-salaries-layout__content']/div[@class='se-player-salaries-main-page']/div[@class='se-player-salaries-main-page__inner']/div[@class='se-player-salaries-main-page__content']/div[@class='se-player-salaries-main-page__filters']/div[@class='se-filters-salaries']/div[1]/div[2]")
        years.click()

    def s22_23(self):
        s22_23 = self.browser.find_element(By.XPATH,"//div[@class='se-select se-select--1col se-select--selected se-select--stretch se-select--size-sm se-select--open se-select--theme-light']//div[8]")
        s22_23.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/khl/money/2022-2023/', "Не правильный год"

    def comands(self):
        comands = self.browser.find_element(By.XPATH,"//body/div[@class='se-player-salaries-layout']/main[@class='se-player-salaries-layout__content']/div[@class='se-player-salaries-main-page']/div[@class='se-player-salaries-main-page__inner']/div[@class='se-player-salaries-main-page__content']/div[@class='se-player-salaries-main-page__filters']/div[@class='se-filters-salaries']/div[2]/div[2]")
        comands.click()

    def admiral(self):
        admiral = self.browser.find_element(By.XPATH,"//div[@class='se-select se-select--1col se-select--stretch se-select--size-sm se-select--open se-select--theme-light']//div[@class='se-select__items']//div[4]")
        admiral.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/khl/money/2022-2023/admiral-11093/', "Не правильная команда"

    def dop_proverka(self):
        dop_proverka = self.browser.find_element(By.XPATH,"//tbody/tr[4]/td[3]/div[1]/div[1]/div[2]")





