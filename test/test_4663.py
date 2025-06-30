from pages.pollpage import PollPage

def test_pollpage(browser):
    polpage = PollPage(browser)
    polpage.open_poll()

    h1 = polpage.h1_poll()
    assert h1 is not None,"Заголовок не найден"

    polpage.reviews()
    assert polpage.reviews(expected_count=30), "Кол-во статей не соответствует ожидаемому"

    eshe = polpage.eshe()
    assert eshe is not None,"Одна из кнопок не найдена или не была нажата"

    material = polpage.material()
    assert material is not None,"Материал не найден"