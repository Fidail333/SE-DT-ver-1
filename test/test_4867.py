from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.tennisWTA import TennisWTA



def test_tennis_wta(browser):
    wta = TennisWTA(browser)
    wta.open()
    wta.reviews()
    wta.news()
    wta.tournir()






