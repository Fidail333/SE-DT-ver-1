from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.figrmedal import FigurkaMedal



def test_figurka_medal(browser):
    figmed = FigurkaMedal(browser)
    figmed.open()
    figmed.menu_nad_logo()
    figmed.plitka_glavn()
    figmed.glavn_news()
    figmed.news()
    figmed.poll()
    figmed.reviews()
    figmed.podval()
    figmed.reklama()
    figmed.medal_za4()
    figmed.vibor_goda()
    figmed.g24()
    figmed.muj()
    figmed.jen()
    figmed.pari()
    figmed.dance()
    figmed.sportsman()
    figmed.uma()


