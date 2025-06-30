from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.livessylefilm import LifeStyFilm


def test_lifestyle_film(browser):
    livestyle_film = LifeStyFilm(browser)
    livestyle_film.open()
    livestyle_film.img()
    livestyle_film.reklama()
    livestyle_film.news()
    livestyle_film.eshe_news()
    livestyle_film.all_news()
    livestyle_film.proverka_news(12)
    livestyle_film.reviews()
    livestyle_film.eshe_reviews()
    livestyle_film.proverka_reviews(7)
    livestyle_film.all_reviews()
    livestyle_film.popylar()
    livestyle_film.podval()
    livestyle_film.reklama()
    livestyle_film.film()
    livestyle_film.h1()
    livestyle_film.reklama()






