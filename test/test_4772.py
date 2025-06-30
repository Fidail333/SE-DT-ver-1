from pages.bombardiers import Bombardiers


def test_bombordiers(browser):
    bombordiers = Bombardiers(browser)
    bombordiers.open()

    menu = bombordiers.menu_nadlogo()
    assert menu is not None, "Меню не найдено или не видимо"

    bombordiers.player()
    assert bombordiers.player(expected_count=3), "Кол-во бомбардиров не соответствует ожидаемому"

    plr_clc = bombordiers.player_click()
    assert plr_clc is not None,"Игрок не найден или не видим"

    bombordiers.how_much_player()
    assert bombordiers.how_much_player(expected_count=233), "Кол-во игроков не соответствует ожидаемому"

    filtri = bombordiers.filti()
    assert filtri is not None, "Фильтр не найден"