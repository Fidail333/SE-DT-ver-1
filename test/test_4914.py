from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.formyla1calend import FormylaCalendar



def test_formyla_calend(browser):
    formcalen = FormylaCalendar(browser)
    formcalen.open()
    formcalen.menu_nad_logo()
    formcalen.h1()
    formcalen.peres()
    formcalen.race()
    formcalen.text()
    formcalen.belgia()


