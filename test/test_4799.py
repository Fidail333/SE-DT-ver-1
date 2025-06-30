from pages.calendarnhl import CalendarNhl
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_calenda_nhl(browser):
    calend = CalendarNhl(browser)
    calend.open()
    calend.tablo()
    calend.plitka_glavn()
    calend.glavn_news()
    calend.news()
    calend.video()
    calend.reviews()
    calend.podval()
    calend.calend()
    calend.h1()
    calend.book()
    #calend.bookes()
    calend.tables()
