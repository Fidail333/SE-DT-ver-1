from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.handballeurop import HandballEurope


def test_handball_europa(browser):
    handball_europe = HandballEurope(browser)
    handball_europe.open()
    handball_europe.menu_nadlogo()
    handball_europe.news()
    handball_europe.reklama()
    handball_europe.reviews()
    handball_europe.photo()
    handball_europe.podval()