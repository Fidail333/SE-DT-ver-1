
from pages.reviewspage import ReviewsPage

def test_reviewspage(browser):
    reviewspage = ReviewsPage(browser)
    reviewspage.open()

    h1 = reviewspage.h1_rev()
    assert h1 is not None, "Заголовок не найден"

    button1 = reviewspage.button_main()
    assert button1 is not None, "Кнопка Главная не найдена"

    button2 = reviewspage.button_readers()
    assert button2 is not None, "Кнопка Читатели не найдена"

    button3 = reviewspage.button_exclusive()
    assert button3 is not None, "Кнопка Эксклюзив не найдена"

    back = reviewspage.back()
    assert back is not None, "Кнопка возврата не найдена"

    photo = reviewspage.photo_vid()
    assert photo is not None, "Кнопка фото не найдена"

    hoceky = reviewspage.hockey_button()
    assert hoceky is not None, "Кнопка хоккея не найдена"

    reviewspage.reviews()
    assert reviewspage.reviews(expected_count=30), "Кол-во статей не соответствует ожидаемому"