from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.matchpagehockey import MatchPageHoc



def test_matchpagehoc(browser):
    matshpage = MatchPageHoc(browser)
    matshpage.open()
    matshpage.menu_nad_logo()
    #matshpage.info_stadium()
    #matshpage.book()
    matshpage.comanda1()
    matshpage.comanda2()
    matshpage.period(3)
    matshpage.pred_vs()
    matshpage.last_game()
    matshpage.stat_vs()
    matshpage.sostoianie()
    matshpage.leaders()
    matshpage.click_leaders()
    matshpage.protocol()
    matshpage.taimeline()
    matshpage.sostavi()
    matshpage.stat_match()
    matshpage.stat_player()
    matshpage.stat_match_player()
    matshpage.nick()
    matshpage.live()
    matshpage.perekli4()
    matshpage.commento()
    matshpage.video()
    matshpage.video_video()