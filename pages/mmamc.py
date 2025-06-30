from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MMAmc:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/live/mma/ufc/')
        sleep(6)

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def filti(self):
        filtri = self.browser.find_element(By.XPATH,"//div[@data-component='matchcenter-filter']")

    def read_news(self):
        read_news = self.browser.find_element(By.XPATH,"//a[contains(text(),'Читать новости')]")
        read_news.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/martial/mma/news/', "Не правильная кнопка новостей"
        self.browser.back()

    def navigator(self):
        navigator = self.browser.find_element(By.XPATH,"//div[@class='se-sport-navigator__competition']")
        navigator.click()

    def belator(self):
        belator = self.browser.find_element(By.XPATH,"//div[@id='react-select-competitions-option-0-2']")
        belator.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/live/mma/bellator/', "Не правильный белатор"

    def prosh(self):
        prosh = self.browser.find_element(By.XPATH,"//a[contains(text(),'Прошедшие')]")
        prosh.click()