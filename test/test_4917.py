from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.f1trassa import FormylaTrasa


def test_formyla_trassa(browser):
    f1_trass = FormylaTrasa(browser)
    f1_trass.open()
    f1_trass.menu_nad_logo()
    f1_trass.h1()
    f1_trass.reklama()
    f1_trass.eshe()
    f1_trass.trassa()
    f1_trass.doroga()
    f1_trass.usa()


