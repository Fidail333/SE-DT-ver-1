from pages.nakazanie import Nakazanie


def test_nakazanie(browser):
    nakazanie = Nakazanie(browser)
    nakazanie.open()

    menu = nakazanie.menu_ndalogo()
    assert menu is not None, "Меню не найдено"

    player = nakazanie.player()
    assert player is not None, "Игрок не найден"

    reklama = nakazanie.reklama()
    assert reklama is not None, "Реклама не найдена"