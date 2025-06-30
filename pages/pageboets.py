from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageBoets:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/tag/hoakin-bakli-25917/')
        sleep(6)

    def info(self):
        info = self.browser.find_element(By.XPATH,"//div[@class='sp-profile-frame-main']")

    def materials(self):
        materials = self.browser.find_element(By.XPATH,"//a[contains(text(),'UFC Ковингтон — Бакли: главный кард боев и трансля')]")
        materials.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/martial/mma/ufc/news/ufc-kovington-bakli-glavnyy-kard-boev-i-translyaciya-turnira-15-dekabrya-2024-gde-smotret-pryamoy-efir-2281605/', "Не правильныу урл"
        self.browser.back()

    def all_news(self):
        all_news = self.browser.find_element(By.XPATH,"//a[@class='se-button se-button--size-big se-last-materials__all']")
        all_news.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/hoakin-bakli-25917/news/', "не правильные все нововтси"
        self.browser.back()

    def news(self):
        news = self.browser.find_element(By.XPATH,"//div[@class='se-page-menu se-page-menu--bt']//a[contains(text(),'Новости')]")
        news.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/hoakin-bakli-25917/news/', "не правильные нововтси"

    def result(self):
        result = self.browser.find_element(By.XPATH,"//a[contains(text(),'Результаты')]")
        result.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/hoakin-bakli-25917/results/',"Не правльные результаты"

    def result_click(self):
        result_click = self.browser.find_element(By.XPATH,"//tbody/tr[4]/td[3]")
        result_click.click()
        sleep(2)
        assert self.browser.current_url == 'https://www.sport-express.ru/live/mma/ufc/event-14805/', "Не правильный урл боя"



