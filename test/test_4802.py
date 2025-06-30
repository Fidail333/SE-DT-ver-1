from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.trenerskhl import TrenerKhl



def test_trenerkhl(browser):
    trennerkhl = TrenerKhl(browser)
    trennerkhl.open()
    trennerkhl.menu_nad_logo()
    trennerkhl.h1()
    trennerkhl.roten()
    trennerkhl.reklama()
    trennerkhl.podval()