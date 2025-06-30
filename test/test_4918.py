from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.basketvtb import BasketVtb


def test_VTB_Basket(browser):
    vtb = BasketVtb(browser)
    vtb.open()
    vtb.menu_nadlogo()
    vtb.news()
    vtb.reklama()
    vtb.reviews()
    vtb.podval()
    vtb.table()
    vtb.reklama()
    vtb.champ()
    vtb.comand()


