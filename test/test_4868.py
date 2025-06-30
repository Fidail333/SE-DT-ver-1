from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.tennisbig import TennisBig



def test_tennis_big(browser):
    big = TennisBig(browser)
    big.open()
    big.plitka()
    big.news()
    big.reviews()
    big.auopen()
    big.h1()
    big.book()








