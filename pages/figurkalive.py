from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FigurkaRu:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/figure-skating/grand-pri-rossii/')
        sleep(6)

    def menu_nad_logo(self):
        menu_nad_logo = self.browser.find_element(By.XPATH,"//div[@class='se-menu-subtop se-menu-subtop--breadcrumb']")

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

    def obsh_za4(self):
        obsh_za4 = self.browser.find_element(By.XPATH,"//a[contains(text(),'Общий зачет')]")
        obsh_za4.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/winter/figure-skating/grand-pri-rossii/2024-2025/standing/men/',"Не правильный зачет"

    def petr(self):
        petr = self.browser.find_element(By.XPATH,"//a[contains(text(),'Петр Гуменник')]")
        petr.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/petr-gumennik-18378/', "Не правльный петр"
        self.browser.back()

    def tag(self):
        tag = self.browser.find_element(By.XPATH,"//div[contains(text(),'Популярные теги')]")






