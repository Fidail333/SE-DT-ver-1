from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.figyrkalednik import FigurkaLednik



def test_figurka_lednik(browser):
    lednik = FigurkaLednik(browser)
    lednik.open()
    lednik.menu_nad_logo()
    lednik.plitka_glavn()
    lednik.glavn_news()
    lednik.news()
    lednik.reviews()
    lednik.podval()
    lednik.allmaterials()
    lednik.materials()