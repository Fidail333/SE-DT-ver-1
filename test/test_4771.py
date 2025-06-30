from pages.calendargame import CalendarGame


def test_calendar_game(browser):
    calendargame = CalendarGame(browser)
    calendargame.open()

    h1 = calendargame.h1()
    assert h1 is not None, "Заголовок не найден"

    calendargame.check_metrika_console_events()
    calendargame.click_and_check_metrika_events()

    match = calendargame.match()
    assert match is not None, "Матч не найден"

    reklama = calendargame.reklama()
    assert reklama is not None, "Реклама не найдена"

