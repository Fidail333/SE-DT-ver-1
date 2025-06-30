from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class MatchPageHoc:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/hockey/L/matchcenter/116730/')
        sleep(6)

    def menu_nad_logo(self):
        menu_nad_logo = self.browser.find_element(By.XPATH,"//div[@class='se-menu-subtop se-menu-subtop--breadcrumb']")

    def info_stadium(self):
        info_stadium = self.browser.find_element(By.XPATH,"//div[@class='sp-mc-match-info']//div[@class='se-titled-block se-titled-block--bg-white']")

    def book(self):
        book = self.browser.find_element(By.XPATH,"//div[@class='sp-matchcenter-board__bookies-rates']")

    def comanda1(self):
        comanda1 = self.browser.find_element(By.XPATH,"//div[@class='sp-matchcenter-board-team-details__team']//a[contains(text(),'Автомобилист')]")
        comanda1.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/avtomobilist-ekaterinburg-272/', "Не правильный урл первой команды"
        self.browser.back()

    def comanda2(self):
        comanda2 = self.browser.find_element(By.XPATH,"//div[@class='sp-matchcenter-board-team-details__team']//a[contains(text(),'Металлург Мг')]")
        comanda2.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/', "не правильный урл второй команды"
        self.browser.back()

    def period(self,count):
        period = self.browser.find_elements(By.XPATH,"//td[@class='sp-matchcenter-score-by-periods__periodScore']")
        assert len(period) == count

    def pred_vs(self):
        pred_vs = self.browser.find_element(By.XPATH,"//div[@class='sp-matchcenter-face-to-face-matches']//div[@class='se-titled-block se-titled-block--bg-white se-titled-block--align-center']")

    def last_game(self):
        last_game = self.browser.find_element(By.XPATH,"//div[@class='sp-mc-last-team-matches']//div[@class='se-titled-block se-titled-block--bg-white se-titled-block--align-center']")

    def stat_vs(self):
        stat_vs = self.browser.find_element(By.XPATH,"//div[@class='sp-mc-faceToface-stats']//div[@class='se-titled-block se-titled-block--bg-white se-titled-block--align-center']")

    def sostoianie(self):
        sostoianie = self.browser.find_element(By.XPATH,"//div[contains(text(),'Текущее состояние команд')]")

    def leaders(self):
        leaders = self.browser.find_element(By.XPATH,"//div[@class='sp-mc-leaders']//div[@class='se-titled-block se-titled-block--bg-white se-titled-block--align-center']")

    def click_leaders(self):
        click_leaders = self.browser.find_element(By.XPATH,"(//img[@title='Да Коста Стефан'])[2]")
        click_leaders.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/stefan-da-kosta-12657/', "не правильный урл тега"
        self.browser.back()

    def protocol(self):
        protocol = self.browser.find_element(By.XPATH,"//a[contains(text(),'Протокол')]")
        protocol.click()
        sleep(2)
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/matchcenter/116730/protocol/', "Не правильный урл протокола"

    def taimeline(self):
        taimeline = self.browser.find_element(By.XPATH,"//div[@class='sp-matchcenter-timeline--inner']")

    def sostavi(self):
        sostavi = self.browser.find_element(By.XPATH,"//div[@class='sp-matchcenter-composition']//div[@class='se-titled-block se-titled-block--bg-white se-titled-block--align-center']")

    def stat_match(self):
        stat_match = self.browser.find_element(By.XPATH,"//div[@class='sp-mc-teams-stats']//div[@class='se-titled-block se-titled-block--bg-white se-titled-block--align-center']")

    def stat_player(self):
        stat_player = self.browser.find_element(By.XPATH,"//a[contains(text(),'Статистика игроков')]")
        stat_player.click()
        sleep(2)
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/matchcenter/116730/stats/', "Не правильная ссылка, статиситки игроков"

    def stat_match_player(self):
        stat_match_player = self.browser.find_element(By.XPATH,"//td[normalize-space()='18:01']")

    def nick(self):
        nick = self.browser.find_element(By.XPATH,"//img[@title='Эберт Ник']")
        nick.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/player/11458/',"Не правильный ссылка тег"
        self.browser.back()

    def live(self):
        live = self.browser.find_element(By.XPATH,"//a[normalize-space()='Live']")
        live.click()
        sleep(2)
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/matchcenter/116730/live/', "не правильный лайв"

    def perekli4(self):
        perekli4 = self.browser.find_element(By.XPATH,"//div[contains(text(),'2 период')]")

    def commento(self):
        commento = self.browser.find_element(By.XPATH,"//a[contains(text(),'Комментарии')]")
        commento.click()
        sleep(2)
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/matchcenter/116730/comments/', "Не правильные комменты урл"

    def video(self):
        video = self.browser.find_element(By.XPATH,"//div[@class='se-page-menu-item']//a[contains(text(),'Видео')]")
        video.click()
        sleep(2)
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/matchcenter/116730/video/', "Не правильное видео"

    def video_video(self):
        video_video = self.browser.find_element(By.XPATH,"//div[@class='se-titled-block se-titled-block--bg-white se-titled-block--align-center']")



