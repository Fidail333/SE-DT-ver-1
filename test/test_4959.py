from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.livestylerten import LifeStyTren


def test_lifestyle_tren(browser):
    livestyle_tren = LifeStyTren(browser)
    livestyle_tren.open()
    livestyle_tren.img()
    livestyle_tren.swipe(4)
    livestyle_tren.reklama()
    livestyle_tren.news()
    livestyle_tren.eshe_news()
    livestyle_tren.all_news()
    livestyle_tren.proverka_news(12)
    livestyle_tren.reviews()
    livestyle_tren.eshe_reviews()
    livestyle_tren.proverka_reviews(7)
    livestyle_tren.all_reviews()
    livestyle_tren.vopros()
    livestyle_tren.popylar()
    livestyle_tren.podval()
    livestyle_tren.reklama()
    livestyle_tren.man()
    livestyle_tren.h1()
    livestyle_tren.reklama()





