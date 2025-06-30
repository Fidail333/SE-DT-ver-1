from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.footballmc import FootballMc



def test_football_mc(browser):
    football_mc = FootballMc(browser)
    football_mc.open()
    football_mc.menu_nad_logo()
    football_mc.reklama()
    football_mc.h1()
    football_mc.vidmaterial()
    football_mc.sport_list()
    football_mc.date()