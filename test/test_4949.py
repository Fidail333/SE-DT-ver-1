from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.texnonews import TexnoNews


def test_texno(browser):
    texno = TexnoNews(browser)
    texno.open()
    texno.menu_nadlogo()
    texno.reklama()
    texno.vid_mat()
    texno.vid_sport()
    texno.knopki()
    texno.eshe()
    texno.spisok(60)