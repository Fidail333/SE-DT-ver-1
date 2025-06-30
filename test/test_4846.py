from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.olimpicfootballmedal import FootballMedal



def test_football_medal(browser):
    footmed = FootballMedal(browser)
    footmed.open()
    footmed.menu_nadlogo()
    #footmed.selector()
    #footmed.voleyball()
    footmed.selec2()
    footmed.po_date()
    footmed.title()
    footmed.h1()
    footmed.prov()