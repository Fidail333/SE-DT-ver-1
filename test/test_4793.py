from pages.stavki import Stavki
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_stavki(browser):
    stavki = Stavki(browser)
    stavki.open()
    stavki.mosaik()
    stavki.glavn_news()
    stavki.reviews()
    stavki.news()
    stavki.lideri()


