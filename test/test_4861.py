from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.biatlonmedal import BiatlonMir



def test_biatlon_medal(browser):
    biatlon = BiatlonMir(browser)
    biatlon.open()
    biatlon.menu_nad_logo()
    biatlon.plitka_glavn()
    biatlon.glavn_news()
    biatlon.news()
    biatlon.reviews()
    biatlon.podval()
    biatlon.medal_za4()
    biatlon.medal_za4()
    biatlon.god24()
    biatlon.content()
    biatlon.france()
    biatlon.myj()
    biatlon.jen()
    biatlon.smesh()
    biatlon.jen()
    biatlon.displ()
    biatlon.estafet()
    biatlon.proverka(3)
    biatlon.sportsman()
    biatlon.sport()

