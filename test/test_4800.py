from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.hocckeystat import HocckeyStat


def test_hocckeystat(browser):
    hockey = HocckeyStat(browser)
    hockey.open()
    hockey.menu_nad_logo()
    hockey.tablo()
    hockey.plitka_glavn()
    hockey.glavn_news()
    hockey.news()
    hockey.video()
    hockey.reviews()
    hockey.podval()
    hockey.poll()
    hockey.stat()
    hockey.h1()
    hockey.kevin()
    hockey.comandni()
    hockey.playoff()
