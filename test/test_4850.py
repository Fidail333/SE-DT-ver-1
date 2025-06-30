from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.mmamc import MMAmc



def test_mma_mc(browser):
    mma_mc = MMAmc(browser)
    mma_mc.open()
    mma_mc.menu_nadlogo()
    mma_mc.h1()
    mma_mc.filti()
    mma_mc.read_news()
    mma_mc.navigator()
    mma_mc.belator()
    mma_mc.prosh()

