from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.rpltable import RplTable



def test_rpl_table(browser):
    rpl_table = RplTable(browser)
    rpl_table.open()
    rpl_table.h1()
    rpl_table.spartak()
    rpl_table.player()
    rpl_table.reklama()
    rpl_table.poloj_comand()
    rpl_table.select()
    rpl_table.h2()
    rpl_table.tour(38)
    rpl_table.spa_ore()
    rpl_table.book()
    rpl_table.zen()

