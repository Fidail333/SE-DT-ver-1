from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.biatlonkybok import BiatlonKybok



def test_biatlon_mir(browser):
    biatlon_kybok = BiatlonKybok(browser)
    biatlon_kybok.open()
    biatlon_kybok.menu_nad_logo()
    biatlon_kybok.plitka_glavn()
    biatlon_kybok.news()
    biatlon_kybok.reviews()
    biatlon_kybok.glavn_news()
    biatlon_kybok.podval()
    biatlon_kybok.obsh_za4()
    biatlon_kybok.h1()
    biatlon_kybok.nation()
    biatlon_kybok.strani(35)
    biatlon_kybok.usa()
    biatlon_kybok.knopa()
    biatlon_kybok.reklama()


