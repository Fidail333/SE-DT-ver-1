from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.voleyballeuro import VoleyballEuro


def test_voleyball_euro(browser):
    vol_euro = VoleyballEuro(browser)
    vol_euro.open()
    vol_euro.menu_nadlogo()
    vol_euro.news()
    vol_euro.reklama()
    vol_euro.reviews()
    vol_euro.photo()
    vol_euro.podval()
    vol_euro.scrolsmi()
    vol_euro.smi()