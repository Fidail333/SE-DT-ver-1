from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.golpassfootball import FootbalGolPas


def test_rpl_gol(browser):
   gol_pass = FootbalGolPas(browser)
   gol_pass.open()
   gol_pass.top3(3)
   gol_pass.reklama()
   gol_pass.asist()
   gol_pass.reklama()
   gol_pass.proverka1()

