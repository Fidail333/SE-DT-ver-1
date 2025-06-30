from pages.register import Registe
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_registers(browser):
    register = Registe(browser)
    register.open()
    register.menu_nad_logo()

