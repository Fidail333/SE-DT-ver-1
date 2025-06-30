from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.livestylemoney import LifeStyMoney


def test_lifestyle_money(browser):
    livestyle_money = LifeStyMoney(browser)
    livestyle_money.open()
    livestyle_money.img()
    livestyle_money.reklama()
    livestyle_money.news()
    livestyle_money.eshe_news()
    livestyle_money.all_news()
    livestyle_money.proverka_news(12)
    livestyle_money.reviews()
    livestyle_money.eshe_reviews()
    livestyle_money.proverka_reviews(7)
    livestyle_money.all_reviews()
    livestyle_money.popylar()
    livestyle_money.podval()
    livestyle_money.reklama()
    livestyle_money.money()
    livestyle_money.h1()
    livestyle_money.reklama()






