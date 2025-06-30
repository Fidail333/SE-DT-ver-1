from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.handball import Handball


def test_handball(browser):
    handball = Handball(browser)
    handball.open()
    handball.menu_nadlogo()
    handball.news()
    handball.reklama()
    handball.reviews()
    handball.photo()
    handball.podval()