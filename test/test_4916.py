from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.f1pilot import FormylaPailot



def test_formyla_pilot(browser):
    f1_pilot = FormylaPailot(browser)
    f1_pilot.open()
    f1_pilot.text()
    f1_pilot.menu_nad_logo()
    #f1_pilot.oscar()
    #f1_pilot.comand()
    #f1_pilot.eshe()
    #f1_pilot.pilot()
    #f1_pilot.h1()
    #f1_pilot.bottas()
    #f1_pilot.mers()

