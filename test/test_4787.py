from pages.rss import Rss
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_rss(browser):
    rss = Rss(browser)
    rss.open()
    rss.h1()
    rss.rss(12)
    rss.foot_rss()
    rss.proverka()
    rss.zag()
