from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MMArait:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/fighting/mma/ufc/2024/ratings/men/')
        sleep(6)

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def jen(self):
        jen = self.browser.find_element(By.XPATH,"//div[@class='se-buttons-toggle-item']")
        jen.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/fighting/mma/ufc/2024/ratings/women/', "не правильный жен"

    def shef(self):
        shef = self.browser.find_element(By.XPATH,"//a[contains(text(),'Валентина Шевченко')]")
        shef.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/valentina-shevchenko-mma-25327/', "Не правильный тег"




