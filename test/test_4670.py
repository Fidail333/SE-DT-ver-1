from pages.detalpoll import DetalPoll
from selenium.webdriver.common.by import By

def test_detalpoll(browser):
    detalpoll = DetalPoll(browser)
    detalpoll.open_detal_poll()
    detalpoll.menu_nadlogo()
    detalpoll.button_poll()
    detalpoll.smi2()
    detalpoll.dop_menu()
    detalpoll.comands()
    detalpoll.h1()
    detalpoll.toronto_click()
    detalpoll.pitsburg_click()
    detalpoll.boston_click()