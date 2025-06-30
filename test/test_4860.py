from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.figyrkaitogi import FigurkaItogi



def test_figurka_itogi(browser):
    itogifig = FigurkaItogi(browser)
    itogifig.open()
    itogifig.h1()
    itogifig.knopki()
    itogifig.vkladki()
    itogifig.final()
    itogifig.sportsmn()
    itogifig.reklama()
    itogifig.book()
    itogifig.tegi()
