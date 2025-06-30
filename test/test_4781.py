from pages.tennisraiting import TennisRaiting



def test_tenisraiting(browser):
    tenisraiting = TennisRaiting(browser)
    tenisraiting.open()

    menu = tenisraiting.menu()
    assert menu is not None, "Меню не найдено или не видимо"

    reklama = tenisraiting.reklama()
    assert reklama is not None, "Реклама не найдена"

    proverka = tenisraiting.verify_all_elements()
    assert proverka,"Найдены не все элементы"

    select = tenisraiting.selector()
    assert select is not None, "Нет селектора или не выбран правльный"

    tenisraiting.how_much()
    assert tenisraiting.how_much(expected_count=62), "Не правильное кол-во игроков"



