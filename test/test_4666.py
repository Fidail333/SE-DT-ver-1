from pages.newsphoto import NewsPhoto


def test_detalphoto(browser):
    newsphoto = NewsPhoto(browser)
    newsphoto.open_photo_news()

    menu = newsphoto.menu_nadlogo()
    assert menu is not None, "Меню не найдено"

    h1 = newsphoto.h1()
    assert h1 is not None, "Заголовок не найден"

    reklama = newsphoto.rekalama()
    assert reklama is not None, "Реклама не найдена"

    share = newsphoto.click_share()
    assert share is not None, "Кнока поделиться не найдена"

    newsphoto.sociaty()
    assert newsphoto.sociaty (expected_count=5), "Кол-во статей не соответствует ожидаемому"

    tags = newsphoto.tags()
    assert tags is not None, "Теги не найдены"

    stat = newsphoto.stat()
    assert stat is not None, "Статистика не найдена"