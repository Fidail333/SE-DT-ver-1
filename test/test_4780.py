from pages.tenismatch import TenisMatch


def test_tenismatch(browser):
    tenismatch = TenisMatch(browser)
    tenismatch.open()

    menu = tenismatch.menu()
    assert menu is not None, "Меню не найдено или не видно"

    name = tenismatch.name_of_turnir()
    assert name is not None, "Название турнира не найдено или не было кликнуто"

    reklama = tenismatch.reklama()
    assert reklama is not None, "Реклама не найдена"

    selector = tenismatch.selector()
    assert selector is not None, "Селектор не найден или не переключен"

    vibor = tenismatch.vibor()
    assert vibor is not None, "Турнир не найден"