from pages.detalnews import DetalNews

def test_detalnews(browser):
    detalnews = DetalNews(browser)
    detalnews.open_detal_news()

    menu = detalnews.menu_nadlogo()
    assert menu is not None, "Меню не найдено"

    h1 = detalnews.h1()
    assert h1 is not None,"Заголовок не найден"

    rekalama = detalnews.rekalama()
    assert rekalama is not None,"Реклама не найдена"

    autor = detalnews.autor()
    assert autor is not None,"Автор не найден"

    comand = detalnews.comand()
    assert comand is not None,"Блок полоэение команд - не найден"

    news = detalnews.block_news()
    assert news is not None,"Блок с новостями не найден"

    obsh = detalnews.obsh()
    assert obsh is not None,"Блок самые обсуждаемые не выводится"

    table = detalnews.table()
    assert table is not None,"Табликцп переходов не найдена"

    commet = detalnews.block_comment()
    assert commet is not None,"Комментарии не найдены"