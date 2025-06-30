from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.footballmel1 import FootballMel1



def test_football_mel1(browser):
    mel1 = FootballMel1(browser)
    mel1.open()
    mel1.menu_nadlogo()
    mel1.h1()
    mel1.foltri()
    mel1.block()
    mel1.foltri()
    mel1.reklama()