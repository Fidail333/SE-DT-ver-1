from pages.tegplayer import Taglayer
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_tagplayer(browser):
    tagplayer = Taglayer(browser)
    tagplayer.open()
    tagplayer.menu_nadlogo()
    tagplayer.table(18)
    tagplayer.o_sportsmen()
    tagplayer.biograf()
    tagplayer.allmaterials()
    tagplayer.reklama()
    tagplayer.perexod()
    tagplayer.perexod_next()
