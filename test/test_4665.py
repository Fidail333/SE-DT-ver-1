from pages.detalreviews import DetalReviews

def test_detalreviews(browser):
    detalreviews = DetalReviews(browser)
    detalreviews.open_detal_reviews()

    menu = detalreviews.menu_nadlogo()
    assert menu is not None, "Меню не найдено"

    h1 = detalreviews.h1()
    assert h1 is not None, "Заголовок не найден"

    reklama = detalreviews.rekalama()
    assert reklama is not None, "Реклама не найдена"

    autor = detalreviews.autor()
    assert autor is not None, "Автор не найден"

    comand = detalreviews.comand()
    assert comand is not None,"Положение команд блок не найден"

    tags = detalreviews.tags()
    assert tags is not None, "Теги не найдены"

    like = detalreviews.like()
    assert like is not None, "Блок с лайками не найден"

    footer = detalreviews.footer()
    assert footer is not None, "Подвал не найден"

    calendar = detalreviews.calendar()
    assert calendar is not None, "Календарь не найден"