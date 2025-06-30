from pages.tablecomands import TableComands

def test_tablecomands(browser):
    tablecomands = TableComands(browser)
    tablecomands.open()

    h1 = tablecomands.h1()
    assert h1 is not None, "Заголовок не найден"

    data = tablecomands.data_table()
    assert data is not None, "Дата не найдена или не переключена"

    loko = tablecomands.loko()
    assert loko is not None, "Команда не найдена"

    legend = tablecomands.legend()
    assert legend is not None, "Легенда не найдена"