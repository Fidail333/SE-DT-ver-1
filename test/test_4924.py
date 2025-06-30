from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.voleyballworld import VoleyballWorld


def test_voleyball_world(browser):
    world = VoleyballWorld(browser)
    world.open()
    world.menu_nadlogo()
    world.news()
    world.reklama()
    world.reviews()
    world.photo()
    world.podval()
    world.scrolsmi()
    world.smi()