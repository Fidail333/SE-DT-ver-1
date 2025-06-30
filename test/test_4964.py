from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.rplstat import RplStat



def test_rpl_stat(browser):
    rpl_stat = RplStat(browser)
    rpl_stat.open()
    rpl_stat.top3(3)
    rpl_stat.tukavin()
    rpl_stat.ska()
    rpl_stat.ronaldo()
    rpl_stat.reklama()
    rpl_stat.asist()
