from pages.cardplayer import CardPlayer



def test_cardpayer(browser):
    cardpayer = CardPlayer(browser)
    cardpayer.open()

    menu = cardpayer.menu()
    assert menu is not None, "Меню не найдено или не видимо"

    proverka = cardpayer.verify_all_elements()
    assert proverka,"Найдены не все элементы"

    bio = cardpayer.bio()
    assert bio is not None, "Био не найдено"

    click_info = cardpayer.click_info()
    assert click_info is not None, "Кнопки команды и вида спорта не найдены"

    btn_click = cardpayer.button_click()
    assert btn_click is not None, "Кнопки не найдены или не видны"

    reklama = cardpayer.reklama()
    assert reklama is not None, "Реклама не найдена"

    next = cardpayer.next_page()
    assert next is not None, "Нет кнопки переключения страниц"