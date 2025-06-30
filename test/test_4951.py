from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.texnodota import TexnoDota


def test_texno_dota(browser):
    texno_dota = TexnoDota(browser)
    texno_dota.open()
    texno_dota.menu_nadlogo()
    texno_dota.news()
    texno_dota.reklama()
    texno_dota.reviews()
    texno_dota.podval()