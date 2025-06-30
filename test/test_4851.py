from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.boetsmma import MMAboets



def test_mma_boets(browser):
    boetsmma = MMAboets(browser)
    boetsmma.open()
    boetsmma.menu_nadlogo()
    boetsmma.h1()
    boetsmma.filtri()
    boetsmma.viktor()
    boetsmma.reklama()
