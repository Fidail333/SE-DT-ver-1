from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class Taglayer:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/tag/krishtianu-ronaldu-973/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, "//div[@class='se-menu-subtop se-menu-subtop--main']")

    def table(self,count):
        table = self.browser.find_elements(By.XPATH,"//td")
        assert len(table) == count

    def o_sportsmen(self):
        o_sportsmen = self.browser.find_element(By.XPATH,"//a[contains(text(),'Все о спортсмене')]")
        o_sportsmen.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/L/player/2283/seasons/2025-2026/', "Не правильный урл кнопки"
        self.browser.back()

    def biograf(self):
        biograf = self.browser.find_element(By.XPATH,"//a[contains(text(),'Биография')]")
        biograf.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/england/reviews/kratkaya-biografiya-krishtianu-ronaldu-detstvo-klubnaya-i-mezhdunarodnaya-karera-lichnaya-zhizn-1946597/', "не правильная ссылка биографии"
        self.browser.back()

    def allmaterials(self):
        allmaterials = self.browser.find_element(By.XPATH,"//h2[contains(text(),'Все материалы')]")

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_159523747962947596']")

    def perexod(self):
        perexod = self.browser.find_element(By.XPATH,"//a[normalize-space()='5']")
        perexod.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/krishtianu-ronaldu-973/page5/',"Не правильная страница"

    def perexod_next(self):
        perexod_next = self.browser.find_element(By.XPATH,"//a[contains(text(),'Далее')]")
        perexod_next.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/krishtianu-ronaldu-973/page6/', "Перехол на следующую страницу не правильный"

