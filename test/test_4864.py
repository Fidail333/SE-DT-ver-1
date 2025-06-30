from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.lijimir import LijiMir



def test_biatlon_mir(browser):
    mirl = LijiMir(browser)
    mirl.open()
    mirl.menu_nad_logo()
    mirl.plitka_glavn()
    mirl.glavn_news()
    mirl.news()
    mirl.reviews()
    mirl.podval()
    mirl.click()
    mirl.material_filtr()
    mirl.vid()
    mirl.knop()
    mirl.glavn()
    mirl.chital()
    mirl.exlisv()
    mirl.reklama()




