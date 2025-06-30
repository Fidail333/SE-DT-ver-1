from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.lifestyle import LifeStyle


def test_lifestyle(browser):
    lyfestyle = LifeStyle(browser)
    lyfestyle.open()
    lyfestyle.img()
    lyfestyle.swipe(4)
    lyfestyle.reklama()
    lyfestyle.news()
    lyfestyle.eshe_news()
    lyfestyle.all_news()
    lyfestyle.proverka_news(12)
    lyfestyle.reviews()
    lyfestyle.eshe_reviews()
    lyfestyle.proverka_reviews(7)
    lyfestyle.all_reviews()
    lyfestyle.vopros()
    lyfestyle.popylar()
    lyfestyle.podval()
    lyfestyle.recept()
    lyfestyle.h1()
    lyfestyle.reklama()
    lyfestyle.h2()



