from itertools import count

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BiatlonMir:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/biathlon/chempionat-mira/')
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

    def medal_za4(self):
        medal_za4 = self.browser.find_element(By.XPATH,"//a[contains(text(),'Медальный зачет')]")
        medal_za4.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/winter/biathlon/chempionat-mira/2024-2025/medals/teams/all/', "Не правильный медальный зачет"

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def god24(self):
        self.browser.get('https://www.sport-express.ru/winter/biathlon/chempionat-mira/2023-2024/medals/teams/all/')
        sleep(6)

    def content(self):
        content = self.browser.find_element(By.XPATH,"//div[@class='se-competition-titled-block__content']")

    def france(self):
        france = self.browser.find_element(By.XPATH,"//div[contains(text(),'Франция')]")
        france.click()

    def myj(self):
        muj = self.browser.find_element(By.XPATH,"//a[contains(text(),'Муж')]")
        muj.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/winter/biathlon/chempionat-mira/2023-2024/medals/teams/men/', "не правльный муж"

    def jen(self):
        jen = self.browser.find_element(By.XPATH,"//a[@class='se-buttons-toggle-item'][contains(text(),'Жен')]")
        jen.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/winter/biathlon/chempionat-mira/2023-2024/medals/teams/women/', "Не правильный жен"

    def smesh(self):
        sesh = self.browser.find_element(By.XPATH,"//a[contains(text(),'Смеш')]")
        sesh.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/winter/biathlon/chempionat-mira/2023-2024/medals/teams/mixed/', "Не правильный смеш"

    def displ(self):
        displ = self.browser.find_element(By.XPATH,"//div[@class='se-select__value-container']")
        displ.click()

    def estafet(self):
        estafet = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__filter']//div[6]")
        estafet.click()
        sleep(4)

    def proverka(self,count):
        proverka = self.browser.find_elements(By.XPATH,"//div[@class='sp-medals-page-bycountry__name']")
        assert len(proverka) == count

    def sportsman(self):
        sportsman = self.browser.find_element(By.XPATH,"//a[@class='se-buttons-toggle-item sp-medals-page-filter__sportsman']")
        sportsman.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/winter/biathlon/chempionat-mira/2023-2024/medals/players/men/', "Не правильный спортсмен"

    def sport(self):
        sport = self.browser.find_element(By.XPATH,"//a[contains(text(),'Йоханнес Бе')]")
        sport.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/yohannes-be-11383/', "Неправильный спортсмен"







