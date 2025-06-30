from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.mmacalend import MMAcalend



def test_MMAcalend(browser):
    mmacal = MMAcalend(browser)
    mmacal.open()
    mmacal.menu_nadlogo()
    mmacal.h1()
    mmacal.filtr1()
    mmacal.aca()
    mmacal.ves()
    mmacal.hightves()

