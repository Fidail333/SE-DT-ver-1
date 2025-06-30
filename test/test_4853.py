from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.pagefight import PageFight



def test_page_boets(browser):
    page_fight = PageFight(browser)
    page_fight.open()
    page_fight.srav_stat()
    page_fight.spisok_knopok()
    page_fight.last_fight()
    page_fight.rulian()
    page_fight.kori()
    page_fight.stat()
    #page_fight.podbr_stat()
    page_fight.bolshe_po_teme()
    page_fight.vse_boi()
    #page_fight.open_boi()
    page_fight.legend()


