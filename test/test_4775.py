from pages.srball import SrBall


def test_srball(browser):
    srball = SrBall(browser)
    srball.open()

    srball.player()
    assert srball.player(expected_count=3), "Кол-во бомбардиров не соответствует ожидаемому"

    plr_clc = srball.player_click()
    assert plr_clc is not None, "Игрок не найден или не видим"

    srball.how_much_player()
    assert srball.how_much_player(expected_count=242), "Кол-во игроков не соответствует ожидаемому"

    filtri = srball.filti()
    assert filtri is not None, "Фильтр не найден"