from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.basketeuro import BasketEuro


def test_EURO_Basket(browser):
    euro = BasketEuro(browser)
    euro.open()
    euro.menu_nadlogo()
    euro.reklama()
    euro.photo()
    euro.podval()
    euro.news()
    euro.reviews()
