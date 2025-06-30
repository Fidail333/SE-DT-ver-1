from pages.zarpalti import Zarplati
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_zp(browser):
    zp = Zarplati(browser)
    zp.open()
    zp.menu_nadlogo()
    zp.h1()
    zp.spisok(30)
    zp.knopka()
    zp.zp()
    zp.h2()
    zp.filtri()
    zp.years()
    zp.s22_23()
    zp.comands()
    zp.admiral()
    zp.dop_proverka()