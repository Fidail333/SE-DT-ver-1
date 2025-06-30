from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.voleyballchamp import VoleyballChamp


def test_voleyball_champ(browser):
    champ_voley = VoleyballChamp(browser)
    champ_voley.open()
    champ_voley.menu_nadlogo()
    champ_voley.news()
    champ_voley.reklama()
    champ_voley.reviews()
    champ_voley.photo()
    champ_voley.podval()
    champ_voley.scrolsmi()
    champ_voley.smi()