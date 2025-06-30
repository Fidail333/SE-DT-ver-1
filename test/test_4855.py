from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.figurkakalend import FigurkaKalend



def test_figurka_calend(browser):
    fig_cal = FigurkaKalend(browser)
    fig_cal.open()
    fig_cal.menu_nad_logo()
    fig_cal.plitka_glavn()
    fig_cal.glavn_news()
    fig_cal.news()
    fig_cal.video()
    fig_cal.reviews()
    fig_cal.poll()
    fig_cal.podval()
    fig_cal.calendar()
    fig_cal.h1()
    fig_cal.tag()
    #fig_cal.book()


