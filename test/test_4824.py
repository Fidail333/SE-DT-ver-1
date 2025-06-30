from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.eurohockey import EuroHockey



def test_eurohockey(browser):
    eurohockey = EuroHockey(browser)
    eurohockey.open()
    eurohockey.h1()
    eurohockey.menu_nad_logo()
    eurohockey.filtri()
    eurohockey.book()
    eurohockey.perexod()