from selenium.webdriver.common.by import By
from time import sleep


class DetalPoll:

    def __init__(self, browser):
        self.browser = browser

    def open_detal_poll(self):
        self.browser.get('https://www.sport-express.ru/hockey/nhl/poll/kakoy-klub-nhl-s-dvumya-i-bolee-rossiyanami-v-sostave-vam-naibolee-interesen-2188058/')
        sleep(6)

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')
        sleep(5)

    def button_poll(self):
        button_poll = self.browser.find_element(By.XPATH, "//button[@class='se-button se-poll-widget__button-discussion se-poll-widget__bottomItem se-button--size-big']")

    def smi2(self):
        smi2 = self.browser.find_element(By.XPATH,"//div[@id='adfox_163825619969794638']")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-menu-subtop__link']")
        dop_menu.click()

    def comands(self):
        comands = self.browser.find_element(By.XPATH,"(//a[contains(text(),'Команды')])[1]")
        self.browser.get('https://www.sport-express.ru/hockey/L/nhl/2024-2025/teams/')
        sleep(6)
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/nhl/2024-2025/teams/', "Не правильнвый урл команд"

    def h1(self):
        h1 = self.browser.find_element(By.XPATH, "//div[@class='sp-page__title']//h1")

    def toronto_click(self):
        toronto_click = self.browser.find_element(By.XPATH,"(//a[contains(text(),'Состав')])[10]")
        toronto_click.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/toronto-meypl-livz-1932/players/', "Не правильная ссылка комманды"
        self.browser.back()

    def pitsburg_click(self):
        pitsburg_click = self.browser.find_element(By.XPATH,"((//a[contains(text(),'Календарь')])[16]")
        pitsburg_click.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/nhl/2024-2025/calendar/?team=50', "Не правильная ссылка календаря"
        self.browser.back()


    def boston_click(self):
        boston_click = self.browser.find_element(By.XPATH,"(//a[contains(text(),'Статистика')])[30]")
        boston_click.click()
        sleep(2)
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/anahaym-daks-2664/players-stats/', "Не правильный урл статистики"

