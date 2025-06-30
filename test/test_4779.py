from pages.stadions import Stadion


def test_stadion(browser):
    stadion = Stadion(browser)
    stadion.open()

    h1 = stadion.h1()
    assert h1 is not None, "Заголовок не найден"

    click = stadion.click()
    assert click is not None, "Стадион не найден или не был кликнут"

    stadion.stadium()
    assert stadion.stadium(expected_count=234), "Не правильное кол-во стадионов"

    click_comand = stadion.click_comand()
    assert click_comand is not None, "Команда не найдена или не кликнута"

    smi2 = stadion.smi2()
    assert smi2 is not None, "Блок СМИ не найден"

    click_area = stadion.click_area()
    assert click_area is not None, "ЦСКА не найдено"

    season = stadion.season()
    assert season is not None, "Селектор сезона не найден или не был кликнут"

    h1 = stadion.h1()
    assert h1 is not None, "Заголовок не найден"

    stadion.stadium()
    assert stadion.stadium(expected_count=198), "Не правильное кол-во стадионов"

    click = stadion.click()
    assert click is not None, "Стадион не найден или не был кликнут"

