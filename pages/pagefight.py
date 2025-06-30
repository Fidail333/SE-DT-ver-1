from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageFight:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/live/mma/ufc/event-14640/')
        sleep(6)

    def spisok_knopok(self):
        spisok_knopok = self.browser.find_element(By.XPATH, "//div[@class='sp-matchcenter-event-page__buttons']")

    def srav_stat(self):
        srav_stat = self.browser.find_element(By.XPATH,"//div[@class='se-matchcenter-event-comparative-statistic-params']")

    def last_fight(self):
        last_fight = self.browser.find_element(By.XPATH,"//div[@class='sp-matchcenter-event-last-fight']")

    def rulian(self):
        rulian = self.browser.find_element(By.XPATH,"//p[contains(text(),'Раулиан')]")
        rulian.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/raulian-paiva-27821/', "Не правильный рулан"
        self.browser.back()

    def kori(self):
        kori = self.browser.find_element(By.XPATH,"//p[contains(text(),'Кори')]")
        kori.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/kori-sendhagen-25243/'
        self.browser.back()

    def stat(self):
        stat = self.browser.find_element(By.XPATH,"//span[@class='se-buttons-toggle-item-advanced__text sp-matchcenter-event-page__button-stats__text']")
        stat.click()

    def podbr_stat(self):
        podbr_stat = self.browser.find_element(By.XPATH,"//div[@class='sp-matchcenter-event-stats__center']")

    def bolshe_po_teme(self):
        bolshe_po_teme = self.browser.find_element(By.XPATH,"//div[@class='se-news-topics-block']")

    def vse_boi(self):
        vse_boi = self.browser.find_element(By.XPATH,"//div[@class='sp-matchcenter-event-all-fights__header-title']")

    def open_boi(self):
        open_boi = self.browser.find_element(By.XPATH,"//div[@class='se-result-battle-score se-result-battle-score--size-sm se-result-battle-score--win-second']//div[@class='se-result-battle-score__result'][normalize-space()='KO']")
        open_boi.click()
        sleep(2)
        assert self.browser.current_url == 'https://www.sport-express.ru/live/mma/ufc/event-14699/#', "Не правльный матч"

    def legend(self):
        legend = self.browser.find_element(By.XPATH,"//div[@class='sp-matchcenter-event-all-fights-mma__markings']")







