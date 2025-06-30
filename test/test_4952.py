from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.texnocs import TexnoCS


def test_texno_cs(browser):
    texno_cs = TexnoCS(browser)
    texno_cs.open()
    texno_cs.menu_nadlogo()
    texno_cs.news()
    texno_cs.reklama()
    texno_cs.reviews()
    texno_cs.podval()