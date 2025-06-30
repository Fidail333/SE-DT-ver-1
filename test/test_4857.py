from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.figyrkanew import FigurkaNew



def test_figurka_new(browser):
    fw = FigurkaNew(browser)
    fw.open()
    fw.filtrs()
    fw.itap()
    fw.america()
    fw.h1()
    fw.sports()
    #fw.text()
    fw.rost()
    fw.flag(152)
    fw.select()
    fw.germany()
    fw.kol_vo(5)


