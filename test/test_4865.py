from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.lijyrussia import LijiRussia



def test_lijy_rus(browser):
    ru_lij = LijiRussia(browser)
    ru_lij.open()
    ru_lij.menu_nad_logo()
    ru_lij.plitka_glavn()
    ru_lij.glavn_news()
    ru_lij.news()
    ru_lij.reviews()
    ru_lij.podval()
    ru_lij.rss()
    ru_lij.allreviews()
    ru_lij.click()
    ru_lij.filtri()



