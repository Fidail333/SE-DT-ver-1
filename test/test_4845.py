from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.footballolimp import FootballOlimp



def test_football_olimp(browser):
    foot_olimp = FootballOlimp(browser)
    foot_olimp.open()
    foot_olimp.menu_nad_logo()
    foot_olimp.h1()
    #foot_olimp.bloki()
    #foot_olimp.news_click()
    #foot_olimp.proverka_tag()
    foot_olimp.switch()
    foot_olimp.august10()
    foot_olimp.proverka()
    ##foot_olimp.vid_sport()
    ##foot_olimp.vid_sport2()
    foot_olimp.prov_bask()

    # ПЕРЕПИСАТЬ ВООБЩЕ