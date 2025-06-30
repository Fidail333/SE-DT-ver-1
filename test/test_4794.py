from pages.it import It
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_it(browser):
    it = It(browser)
    it.open()
    it.menu_nad_logo()
    it.h1()
    it.p()
    it.eshe()
    it.razgovor()
    it.h2()
    it.knopka()
    it.material(60)
