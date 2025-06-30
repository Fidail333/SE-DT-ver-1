from pages.datallive import DetalLive

def test_detallive(browser):
    detallive = DetalLive(browser)
    detallive.open_detal_live()

    menu = detallive.menu_nadlogo()
    assert menu is not None, "Меню не найдено"

    h1 = detallive.h1()
    assert h1 is not None, "Заголовок не найден"

    date = detallive.datelive()
    assert date is not None, "Дата и время не найдено"

    comand = detallive.comand()
    assert comand is not None, "Блок положение команд не найден"

    footer = detallive.podval()
    assert footer is not None, "Подвал не найден"