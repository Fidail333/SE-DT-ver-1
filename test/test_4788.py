from pages.podpiska import Podpiska
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_podpiska(browser):
    podpiska = Podpiska(browser)
    podpiska.open()
    podpiska.h3()
    podpiska.input()
    podpiska.button()
    podpiska.brend()
    podpiska.h1()
    podpiska.text()

