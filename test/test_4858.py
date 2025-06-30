from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.figyrkaeuropa import FigurkaEuropa



def test_figurka_europa(browser):
    figeur = FigurkaEuropa(browser)
    figeur.open()
    figeur.menu_nad_logo()
    figeur.plitka_glavn()
    figeur.glavn_news()
    figeur.news()
    figeur.reviews()
    figeur.poll()
    figeur.podval()
    figeur.photo()
    figeur.new_photo()
    figeur.rss()
    figeur.allnews()
    figeur.allrewiews()
    figeur.dop_menu()
    figeur.comand()
    figeur.title()
    figeur.god()
    figeur.god_24()
    figeur.strani(33)






