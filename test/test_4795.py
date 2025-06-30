from pages.raiting import Raiting
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_rait(browser):
    rait = Raiting(browser)
    rait.open()
    rait.h1()
    rait.nadej()
    rait.spisok()
    rait.olimp()
    rait.reklama()
    rait.knopka()
    rait.proverka(15)
    rait.polojenie()
    rait.eshe()
    rait.golshak()
    rait.reviews()