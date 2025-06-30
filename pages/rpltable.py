from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class RplTable:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/football/L/russia/premier/2023-2024/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Россия. Премьер-лига 2023-2024, турнирные таблицы')]")

    def spartak(self):
        spartak = self.browser.find_element(By.XPATH,"(//a[contains(text(),'Спартак')])[2]")
        spartak.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/L/command/1/', "Не правильный спартак"
        self.browser.back()

    def player(self):
        player = self.browser.find_element(By.XPATH,"//a[contains(text(),'Сауль Гуарирапа')]")
        player.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/L/player/77027/seasons/2025-2026/', "Не правильный бомбардир"
        self.browser.back()

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH, "//div[@id='adfox_15645683733586888']")

    def poloj_comand(self):
        poloj_comand = self.browser.find_element(By.XPATH,"//div[contains(text(),'Положение команд')]")

    def select(self):
        self.browser.get('https://www.sport-express.ru/football/L/russia/premier/2023-2024/calendar/tours/')
        sleep(6)

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Россия. Премьер-лига 2023-2024, расписание матчей,')]")

    def tour(self,count):
        tour = self.browser.find_elements(By.XPATH,"//th")
        assert len(tour) == count

    def spa_ore(self):
        spa_ore = self.browser.find_element(By.XPATH,"//tbody/tr[7]/td[3]/div[1]/p[1]/a[1]")
        spa_ore.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/rfpl/fbl_match-spartak-orenburg-374050/', "не правильный матч"
        self.browser.back()

    def book(self):
        book = self.browser.find_element(By.XPATH,"//div[@class='se19-main-content__extra']")

    def zen(self):
        zen = self.browser.find_element(By.XPATH,"//tbody/tr[26]/td[2]/div[1]/span[1]/a[1]")
        zen.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/L/command/9/', "Не правильный зенит"

