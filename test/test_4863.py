from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.lijikalend import LijiCelndar



def test_liji_calend(browser):
    liji = LijiCelndar(browser)
    liji.open()
    liji.menu_nad_logo()
    liji.plitka_glavn()
    liji.glavn_news()
    liji.news()
    liji.reviews()
    liji.podval()
    liji.calend()
    liji.filters()
    liji.sprint()
    liji.myj()
    #liji.kol_vo(39)
    liji.jen()
    #liji.kol_vo(27)
    liji.smesh()
    #liji.kol_vo(1)
    #liji.vse()
    #liji.etap()
    #liji.ryka()
    #liji.kol_vo(6)
    #liji.displ()
    #liji.mass()
    #liji.kol_vo(2)




