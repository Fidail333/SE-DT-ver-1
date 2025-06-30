from pages.reklama import Reklama
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_reklama(browser):
    reklama = Reklama(browser)
    reklama.open()
    reklama.everest()
    reklama.click_verest()
    reklama.autor()
    reklama.glv()
    reklama.h1()
    reklama.spisok(16)
    reklama.knopka()
    reklama.spisok2(24)
    reklama.perexod()
