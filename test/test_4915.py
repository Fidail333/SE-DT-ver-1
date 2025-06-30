from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.f1konstr import FormylaKostryktor



def test_formyla_konstryktor(browser):
    f1 = FormylaKostryktor(browser)
    f1.open()
    f1.menu_nad_logo()
    f1.kubok()
    f1.text()

