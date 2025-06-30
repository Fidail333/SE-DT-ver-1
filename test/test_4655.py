
from pages.homepage import HomePage
import logging

logging.basicConfig(level=logging.INFO)

def test_glavn_se(browser):
    homepage = HomePage(browser)
    homepage.open()

    tablo = homepage.tablo_find()
    assert tablo is not None, "Табло не найдено!"

    plitka = homepage.plitka()
    assert plitka is not None, "Блок с плиткой не найден"

    news_block = homepage.news()
    assert news_block is not None, "Блок с новостями не рнайден!"

    homepage.check_metrika_console_events()

    main = homepage.main_news()
    assert main is not  None, "Блок главные новости не найден"

    video = homepage.block_video()
    assert video is not None, "Блок видео не найден или не видим"

    click = homepage.click_video()
    assert click is not None, "Клик не был совершен, либо кнопка не найдена"

    reviews = homepage.block_reviews()
    assert reviews is not None, "Блок статьи не найден"

    reads = homepage.read()
    assert reads is not None, "Блок выбор читателей не найден"

    photo = homepage.block_photo()
    assert photo is not None, "Блок фото не найден"

    reklama = homepage.block_reklama()
    assert reklama is not None, "Блок с рекламой не найден"

    comand = homepage.block_table()
    assert comand is not None, "Блок с положением команд не найден"

    stat = homepage.block_stat()
    assert stat is not None, "Блок статистике не найден"