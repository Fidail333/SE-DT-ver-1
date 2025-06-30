from pages.detalstory import DetalStory


def test_detalstory(browser):
    detalsory = DetalStory(browser)
    detalsory.open_detal_story()

    menu = detalsory.menu_nadlogo()
    assert menu is not None, "Меню не найдено"

    h1 = detalsory.h1()
    assert h1 is not None, "Заголовок не найден"

    social = detalsory.social()
    assert social is not None, "Соц сети не найдены"

    detalsory.material()
    assert detalsory.material(expected_count=16), "Кол-во статей не соответствует ожидаемом, ожидалось 16"

    reviews =  detalsory.reviews()
    assert reviews is not None, "Блок статьи не выводится"

    detalsory.click_reviews()
    assert detalsory.click_reviews(expected_count=22), "Кол-во статей не соответствует ожидаемому, ожидалось 22"

    news = detalsory.news()
    assert news is not None, "Блок новости не найден"

    detalsory.click_news()
    assert detalsory.click_news(expected_count=24), "Кол-во статей не соответствует ожидаемом, ожидалось 24"

    video = detalsory.video()
    assert video is not None, "Блок видео не найден"

    detalsory.click_video()
    assert detalsory.click_video(expected_count=34), "Кол-во статей не соответствует ожидаемому, ожидалось 28"

    photo = detalsory.photo()
    assert photo is not None, "Блок фото не найден"

    detalsory.click_photo()
    assert detalsory.click_photo(expected_count=44), "Кол-во статей не соответствует ожидаемому, ожидалось 32"

    calend = detalsory.calend()
    assert calend is not None, "Календарь не найден"