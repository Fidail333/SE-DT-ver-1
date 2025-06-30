from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.voleyball import Voleyball


def test_voleyball(browser):
    vol = Voleyball(browser)
    vol.open()
    vol.menu_nadlogo()
    vol.news()
    vol.reklama()
    vol.reviews()
    vol.photo()
    vol.podval()
    vol.poll()
    vol.scrolsmi()
    vol.smi()
