from pages.mc1 import Mc1


def test_mc1(browser):
    mc1 = Mc1(browser)
    mc1.open()

    menu = mc1.menu_nadlogo()
    assert menu is not None, "Меню не найдено"

    mc1.check_metrika_console_events()
    mc1.click_and_check_metrika_events()

    btn = mc1.buttons()
    assert btn is not None, "Кнопки не найдены"

    calend = mc1.data_calend()
    assert calend is not None, "Кнопка календаря не найдена"

    seclect = mc1.selector()
    assert seclect is not None, "Селектор не найден или меню"