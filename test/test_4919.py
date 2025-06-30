from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.basketnba import BasketNba


def test_NBA_Basket(browser):
    nba = BasketNba(browser)
    nba.open()
    nba.menu_nadlogo()
    nba.reklama()
    nba.plitka()
    nba.news()
    nba.reviews()
    nba.podval()
    nba.table()
    nba.reklama()
    nba.book()
    nba.match()
