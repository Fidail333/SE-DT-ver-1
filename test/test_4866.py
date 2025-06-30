from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.tennisATP import TennisAtp



def test_tennis_atp(browser):
    tennisatp = TennisAtp(browser)
    tennisatp.open()
    tennisatp.news()
    tennisatp.reklama()
    tennisatp.rait()
    tennisatp.spisok()
    tennisatp.vibor()




