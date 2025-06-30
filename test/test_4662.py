from pages.onlinepage import OnlinePage


def test_onlinepage(browser):
    onlinepage = OnlinePage(browser)
    onlinepage.open_online()

    h1 = onlinepage.h1_online()
    assert h1 is not None, "Заголовк не найден"

    eshe = onlinepage.eshe()
    assert eshe is not None, "Одна из кнопок не найдена или не нажата "

    reklama = onlinepage.reklama()
    assert reklama is not None, "Реклама не найдена"