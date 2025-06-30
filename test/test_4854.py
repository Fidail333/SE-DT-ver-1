from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.figurkalive import FigurkaRu



def test_figurka_ru(browser):
    figr = FigurkaRu(browser)
    figr.open()
    figr.menu_nad_logo()
    figr.plitka_glavn()
    figr.glavn_news()
    figr.news()
    figr.video()
    figr.reviews()
    figr.poll()
    figr.podval()
    figr.obsh_za4()
    figr.petr()
    figr.tag()

