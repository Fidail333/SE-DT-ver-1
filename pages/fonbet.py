from itertools import count

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class Fonbet:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/hockey/khl/')
        sleep(6)
        sleep(3)

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
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/khl/2024-2025/?type=division', "Не правильная талица"

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'FONBET КХЛ. Турнирная таблица')]")

    def vkladki(self,count):
        vkladki = self.browser.find_elements(By.XPATH,"//div[@class='se-page-menu-item']")
        assert len(vkladki) == count

    def spisok_com(self,count):
        spisok_com = self.browser.find_elements(By.XPATH,"//div[@class='sp-team-image']")
        assert len(spisok_com) == count

    def spartak(self):
        spartak = self.browser.find_element(By.XPATH,"//div[@class='sp-team-image-with-name__name']//a[contains(text(),'Спартак')]")
        spartak.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/spartak-hokkey-513/', "Не правильный спартак"
        self.browser.back()

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//a[contains(text(),'Общая')]")
        obsh.click()
        sleep(2)
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/khl/2024-2025/?type=tour', "Не правильный общий"

    def scroll(self):
        scroll = self.browser.find_element(By.XPATH,"//a[contains(text(),'Тесты и квизы')]")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
        sleep(5)

    def smi2(self):
        smi2 = self.browser.find_element(By.XPATH,"//div[@id='adfox_159523826122331374']")

    def next_game(self):
        next_game = self.browser.find_element(By.XPATH,"//div[@class='se-titled-block se-titled-block--bg-white']")
