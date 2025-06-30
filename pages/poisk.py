from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

class Poisk:

    def __init__(self, browser):
        self.browser = browser


    def open(self):
        self.browser.get('https://www.sport-express.ru/search/?sw=')
        sleep(6)

    def menu_nad_logo(self):
        menu_nad_logo = self.browser.find_element(By.XPATH, "//div[@class='se-menu-subtop se-menu-subtop--main']")

    def input(self):
        input = self.browser.find_element(By.XPATH,"//input[@placeholder='Поиск:']")
        input.clear()
        input.send_keys("Футбол")
        input.send_keys(Keys.ENTER)
        sleep(3)
        assert self.browser.current_url == 'https://www.sport-express.ru/search/?sw=%D4%F3%F2%E1%EE%EB&sportType=&kolonki=&perPage=30&date_from=&date_to=', "Не правильный поиск"

    def zag(self):
        zag = self.browser.find_element(By.XPATH,"//label[contains(text(),'Поиск по заголовкам')]")
        zag.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/search/?sportType=&kolonki=&perPage=30&date_from=&date_to=&st=1&sw=%D4%F3%F2%E1%EE%EB', "Не правильная кнопка1"
        self.browser.back()

    def tochno(self):
        tochno = self.browser.find_element(By.XPATH,"//label[contains(text(),'Точное соответствие')]")
        tochno.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/search/?sportType=&kolonki=&perPage=30&date_from=&date_to=&exact=1&sw=%D4%F3%F2%E1%EE%EB', "Не правильное точное"
        self.browser.back()

    def filtri(self):
        filtri = self.browser.find_element(By.XPATH,"//ul[@class='se19-search__options']")

    def pat(self):
        pat = self.browser.find_element(By.XPATH,"//div[@class='white_block clearfix']//a[@class='se19-pagination__point'][normalize-space()='5']")
        pat.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/search/page5/?sw=%D4%F3%F2%E1%EE%EB&sportType=&kolonki=&perPage=30&date_from=&date_to=', "Не 5 стр"

    def dalee(self):
        dalee = self.browser.find_element(By.XPATH,"//div[@class='white_block clearfix']//a[@class='se19-pagination__point'][contains(text(),'Далее')]")
        dalee.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/search/page6/?sw=%D4%F3%F2%E1%EE%EB&sportType=&kolonki=&perPage=30&date_from=&date_to=', "Не 6 стр"
