from pages.detalvideo import DetalVideo


def test_detalvideo(browser):
    detalvideo = DetalVideo(browser)
    detalvideo.open_detal_video()

    menu = detalvideo.menu_nadlogo()
    assert menu is not None, "Меню не выводится"

    h1 = detalvideo.h1()
    assert h1 is not None, "Заголовок не выводится"

    reklama = detalvideo.rekalama()
    assert reklama is not None, "Реклама не выводится"

    datet = detalvideo.date()
    assert datet is not None, "Дата не отображается"

    bread = detalvideo.bread()
    assert bread is not None, "Хлебные крошки не выводятся"

    stadion2 = detalvideo.stadion()
    assert stadion2 is not None, "Кнопка стадиона не найдена"