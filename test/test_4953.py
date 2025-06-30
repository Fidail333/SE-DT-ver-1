from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.texnolol import TexnoLOL


def test_texno_lol(browser):
    texno_lol = TexnoLOL(browser)
    texno_lol.open()
    texno_lol.menu_nadlogo()
    texno_lol.news()
    texno_lol.reklama()
    texno_lol.reviews()
    texno_lol.podval()