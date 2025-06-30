from pages.game import Game
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_game(browser):
    game = Game(browser)
    game.open()
    game.h1()
