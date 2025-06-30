from pages.statisticplayer import StatisticPlayer


def test_statisticplayer(browser):
    stplayer = StatisticPlayer(browser)
    stplayer.open()

    menu = stplayer.menu()
    assert menu is not None, "Меню не найдено или не видимо"

    info = stplayer.info()
    assert info is not None, "Инфоромация о спортсмене не найдена"

    match = stplayer.match()
    assert match is not None, "Матчи спортсмена не найдены"

    reklama = stplayer.reklama()
    assert reklama is not None, "Реклама не найдена"

    aponent = stplayer.apponent()
    assert aponent is not None, "Кнопка соперников не найдена"

