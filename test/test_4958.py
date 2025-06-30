from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.lifestylemed import LifeStyleMed
from pages.texnofootball import TexnoFootball


def test_lifestyle_med(browser):
    lifestyle_med = LifeStyleMed(browser)
    lifestyle_med.open()
    lifestyle_med.img()
    lifestyle_med.swipe(4)
    lifestyle_med.reklama()
    lifestyle_med.news()
    lifestyle_med.eshe_news()
    lifestyle_med.all_news()
    lifestyle_med.proverka_news(12)
    lifestyle_med.reviews()
    lifestyle_med.eshe_reviews()
    lifestyle_med.proverka_reviews(7)
    lifestyle_med.all_reviews()
    lifestyle_med.vopros()
    lifestyle_med.popylar()
    lifestyle_med.podval()
    lifestyle_med.reklama()
    lifestyle_med.med()
    lifestyle_med.h1()
    lifestyle_med.reklama()
    lifestyle_med.page2()
    lifestyle_med.h2()




