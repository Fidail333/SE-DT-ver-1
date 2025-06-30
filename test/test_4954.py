from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.texnofootball import TexnoFootball


def test_texno_football(browser):
    texno_football = TexnoFootball(browser)
    texno_football.open()
    texno_football.menu_nadlogo()
    texno_football.news()
    texno_football.reklama()
    texno_football.reviews()
    texno_football.podval()