from pages.mcfootball import McFootball

def test_mcfootball(browser):
    mcfootball = McFootball(browser)
    mcfootball.open()

    reklama = mcfootball.reklama()
    assert reklama is not None,"Реклама не найдена"

    h1 = mcfootball.h1()
    assert h1 is not None, "Заголовок не найден"

    mcfootball.check_metrika_console_events()
    mcfootball.click_and_check_metrika_events()

    btn = mcfootball.buttons()
    assert btn is not None, "Кнопки не найдены"

    calend = mcfootball.data_calend()
    assert calend is not None, "Календарь не найден"

    footer = mcfootball.footer()
    assert footer is not None, "Подвал не найден"

    select = mcfootball.selector()
    assert select is not None, "Проблемы с селектором"