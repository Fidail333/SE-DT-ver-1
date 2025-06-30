from pages.fonbet import Fonbet
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_fonbet(browser):
    fon = Fonbet(browser)
    fon.open()
    fon.glavn_news()
    fon.news()
    fon.video()
    fon.reviews()
    fon.poll()
    fon.podval()
    fon.table()
    fon.h1()
    fon.vkladki(2)
    fon.spisok_com(43)
    fon.spartak()
    fon.obsh()
    fon.scroll()
    fon.smi2()
    fon.next_game()
