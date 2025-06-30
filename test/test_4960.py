from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.livestyledeti import LifeStyDeti


def test_lifestyle_deti(browser):
    livestyle_deti = LifeStyDeti(browser)
    livestyle_deti.open()
    livestyle_deti.img()
    livestyle_deti.swipe(4)
    livestyle_deti.reklama()
    livestyle_deti.news()
    livestyle_deti.eshe_news()
    livestyle_deti.all_news()
    livestyle_deti.proverka_news(12)
    livestyle_deti.reviews()
    livestyle_deti.eshe_reviews()
    livestyle_deti.proverka_reviews(7)
    livestyle_deti.all_reviews()
    livestyle_deti.popylar()
    livestyle_deti.podval()
    livestyle_deti.reklama()
    livestyle_deti.deti()
    livestyle_deti.h1()
    livestyle_deti.reklama()





