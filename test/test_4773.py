from pages.golpas import GolAndPass


def test_golpas(browser):
    golpas = GolAndPass(browser)
    golpas.open()

    menu = golpas.menu_nadlogo()
    assert menu is not None, "Меню не найдено или не видимо"

    golpas.player()
    assert golpas.player(expected_count=3), "Кол-во бомбардиров не соответствует ожидаемому"

    plr_clc = golpas.player_click()
    assert plr_clc is not None, "Игрок не найден или не видим"

    golpas.how_much_player()
    assert golpas.how_much_player(expected_count=323), "Кол-во игроков не соответствует ожидаемому"

    filtri = golpas.filti()
    assert filtri is not None, "Фильтр не найден"