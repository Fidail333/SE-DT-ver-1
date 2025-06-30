from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.raitmma import MMArait



def test_mma_rait(browser):
    raitmma = MMArait(browser)
    raitmma.open()
    raitmma.menu_nadlogo()
    raitmma.h1()
    raitmma.jen()
    raitmma.shef()

