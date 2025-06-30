from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.pageboets import PageBoets



def test_page_boets(browser):
    page_boet = PageBoets(browser)
    page_boet.open()
    #page_boet.info()
    page_boet.materials()
    page_boet.all_news()
    page_boet.news()
    page_boet.result()
    #page_boet.result_click()

