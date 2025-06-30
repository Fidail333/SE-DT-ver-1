from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FigurkaMedal:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/figure-skating/chempionat-mira/')
        sleep(6)

    def menu_nad_logo(self):
        menu_nad_logo = self.browser.find_element(By.XPATH,"//div[@class='se-menu-subtop se-menu-subtop--breadcrumb']")

    def plitka_glavn(self):
        plitka_glavn = self.browser.find_element(By.XPATH, "//div[@class='se-materials-grid-mosaic']")

    def glavn_news(self):
        glavn_news = self.browser.find_element(By.XPATH,'''//div[@class='se-mainnews']//section[@class="se-titled-block"]''')

    def news(self):
        news = self.browser.find_element(By.XPATH, '''//div[@class='se-newsline']//section[@class="se-titled-block"]''')

    def reviews(self):
        reviews = self.browser.find_element(By.XPATH, "//div[contains(text(),'Статьи')]")

    def poll(self):
        poll = self.browser.find_element(By.XPATH, "//section[@class='se-titled-block mb_30']")

    def podval(self):
        podval = self.browser.find_element(By.XPATH, '//footer[@class="se-footer"]')

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")

    def medal_za4(self):
        medal_za4 = self.browser.find_element(By.XPATH,"//a[contains(text(),'Медальный зачет')]")
        medal_za4.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/winter/figure-skating/chempionat-mira/2024-2025/medals/teams/all/', "Не правильный медальный зачет"

    def vibor_goda(self):
        vibor_goda = self.browser.find_element(By.XPATH,"//div[@class='se-sport-navigator__season']")
        vibor_goda.click()

    def g24(self):
        self.browser.get('https://www.sport-express.ru/winter/figure-skating/chempionat-mira/2023-2024/medals/teams/all/')
        sleep(6)

    def muj(self):
        muj = self.browser.find_element(By.XPATH,"//a[contains(text(),'Муж')]")
        muj.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/winter/figure-skating/chempionat-mira/2023-2024/medals/teams/men/', "Не правльный муж"

    def jen(self):
        jen = self.browser.find_element(By.XPATH,"//a[@class='se-buttons-toggle-item'][contains(text(),'Жен')]")
        jen.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/winter/figure-skating/chempionat-mira/2023-2024/medals/teams/women/', "Не правильный жен"

    def pari(self):
        pari = self.browser.find_element(By.XPATH,"//a[contains(text(),'Пары')]")
        pari.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/winter/figure-skating/chempionat-mira/2023-2024/medals/teams/pairs/'

    def dance(self):
        dance = self.browser.find_element(By.XPATH,"//a[contains(text(),'Танцы')]")
        dance.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/winter/figure-skating/chempionat-mira/2023-2024/medals/teams/dance/', "Не правильные танцы"

    def sportsman(self):
        sportsman = self.browser.find_element(By.XPATH,"//a[@class='se-buttons-toggle-item sp-medals-page-filter__sportsman']")
        sportsman.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/winter/figure-skating/chempionat-mira/2023-2024/medals/players/men/', "Не правильный спортсмен"

    def uma(self):
        uma = self.browser.find_element(By.XPATH,"//a[contains(text(),'Юма Кагияма')]")
        uma.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/yuma-kagiyama-20397/', "Не правльный спортсмен"












