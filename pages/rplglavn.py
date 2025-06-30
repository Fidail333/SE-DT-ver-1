from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class FootbalGlavn:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/football/L/russia/premier/2024-2025/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Россия. Премьер-лига 2024-2025, турнирные таблицы')]")

    def comands(self,count):
        comands = self.browser.find_elements(By.XPATH,"//td[@class='left']")
        assert len(comands) == count

    def krilia(self):
        krilia = self.browser.find_element(By.XPATH,"(//a[contains(text(),'Крылья Советов')])[7]")
        krilia.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/L/command/10/', "Не правильные крылья"
        self.browser.back()

    def legend(self):
        legend = self.browser.find_element(By.XPATH,"//font[contains(text(),'В случае равенства очков у двух и более команд мес')]")




