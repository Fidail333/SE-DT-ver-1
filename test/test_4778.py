from pages.treners import Trener


def test_treners(browser):
    treners = Trener(browser)
    treners.open()

    menu = treners.menu()
    assert menu is not None, "Нет меню над лого"

    treners.treners()
    assert treners.treners(expected_count=255), "Не правильное кол-во тренеров"

    click_trener = treners.click_trener()
    assert click_trener is not None, "Тренер не выводится или не совершен клик"

    btn = treners.knopka()
    assert btn is not None, "Кнопка показать еще не найдена или не кликнута"

    treners.treners()
    assert treners.treners(expected_count=339), "Не правильное кол-во тренеров"

    btn = treners.knopka()
    assert btn is not None, "Скрыть еще не найдена или не кликнута"

    treners.treners()
    assert treners.treners(expected_count=255), "Не правильное кол-во тренеров"

    trn = treners.click_trn()
    assert trn is not None, "второй тренер не найден"

    god = treners.god()
    assert god is not None, "Сезон 21-22 не выбрал или не найден"

    h1 = treners.h1()
    assert h1 is not None, "Заголовок не найден"

    reklama = treners.reklama()
    assert reklama is not None, "Реклама не найдена"
