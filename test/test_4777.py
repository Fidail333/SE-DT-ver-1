from pages.comandsdiviz import ComandDiviz

def test_comanddiviz(browser):
    comanddiviz = ComandDiviz(browser)
    comanddiviz.open()

    comanddiviz.deviz()
    assert comanddiviz.deviz(expected_count=4), "Кол-во девезионов не соответствует ожидаемому"

    comands = comanddiviz.comands()
    assert comands is not None, "Не работают кнопки команд"

    reklama = comanddiviz.reklama()
    assert reklama is not None, "Реклама не найдена"

    data = comanddiviz.data()
    assert data is not None, "Не найден селектор с датой"

    comanddiviz.deviz()
    assert comanddiviz.deviz(expected_count=4), "Кол-во девезионов не соответствует ожидаемому"

    h1 = comanddiviz.h1()
    assert h1 is not None, "Заголовок не найден"