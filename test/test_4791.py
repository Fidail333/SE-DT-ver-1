from pages.poisk import Poisk
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_poisk(browser):
    poisk = Poisk(browser)
    poisk.open()
    poisk.menu_nad_logo()
    poisk.input()
    poisk.zag()
    poisk.tochno()
    poisk.filtri()
    poisk.pat()
    poisk.dalee()

