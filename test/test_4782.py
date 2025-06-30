from pages.mmaraiting import MmaRaiting



def test_mmarait(browser):
    mmarait = MmaRaiting(browser)
    mmarait.open()

    menu = mmarait.menu()
    assert menu is not None,"Меню не найдено"

    h1 = mmarait.h1()
    assert h1 is not None, "Заголовок не найден"

    mmarait.boets()
    assert mmarait.boets(expected_count=15), "Количество бойцов не правильное"

    champion = mmarait.champion_panel()
    assert champion is not None, "Чемпион не найден"

    click_fight = mmarait.click_fighter()
    assert click_fight is not None, "Бойцы не найдены или не кликабельны" #ЕСЛИ ТЕСТ УПАЛ БЕЗ СООБЩЕНИЯ ТО ДЕЛО ТУТ, ОШИБКА В КЛИКЕ БОЙЦА
                                                                            #Перекрывает банер, потом придумать что сделать, чтобы не падал просто так

    proverka = mmarait.verify_all_elements()
    assert proverka,"Найдены не все элементы"

    sort = mmarait.sort()
    assert sort is not None, "сортировка не работает"

    select = mmarait.select_aca()
    assert select is not None, "Промоушен АСА не найден"

    mmarait.boets()
    assert mmarait.boets(expected_count=15), "Количество бойцов не правильное"

    reklama = mmarait.reklama()
    assert reklama is not None,"Реклама не найдена"


