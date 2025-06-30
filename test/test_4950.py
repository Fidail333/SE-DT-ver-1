from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.texnoreviews import TexnoRviews


def test_texno_reviews(browser):
    texno_reviews = TexnoRviews(browser)
    texno_reviews.open()
    texno_reviews.menu_nadlogo()
    texno_reviews.h1()
    texno_reviews.reklama()
    texno_reviews.vid_mat()
    texno_reviews.vid_sport()
    texno_reviews.knopki()