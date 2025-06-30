from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.handballworld import HandballWorld


def test_handball_world(browser):
    handball_world = HandballWorld(browser)
    handball_world.open()
    handball_world.menu_nadlogo()
    handball_world.news()
    handball_world.reklama()
    handball_world.reviews()
    handball_world.photo()
    handball_world.podval()