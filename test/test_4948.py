from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.chess import Chess


def test_chess(browser):
    chess = Chess(browser)
    chess.open()
    chess.menu_nadlogo()
    chess.news()
    chess.reklama()
    chess.reviews()
    chess.photo()
    chess.podval()
