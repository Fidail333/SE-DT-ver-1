from pages.info import Info
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_info(browser):
    info = Info(browser)
    info.open()
    info.h1()
    info.priloj()
    info.h2()
    info.imga()

