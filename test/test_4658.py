
from pages.videopage import VideoPage


def test_videopage(browser):
    videopage = VideoPage(browser)
    videopage.open_video()

    h1 = videopage.h1_video()
    assert h1 is not None,"Заголовок не найден"

    button1 = videopage.button_main()
    assert button1 is not None, "Кнопка Главная не найдена"

    button2 = videopage.button_readers()
    assert button2 is not None, "Кнопка Читатели не найдена"

    button3 = videopage.button_exclusive()
    assert button3 is not None, "Кнопка Эксклюзив не найдена"

    back = videopage.back()
    assert back is not None, "Кнопка весь спорт не найдена"

    reklama = videopage.reklama()
    assert reklama is not None,"Реклама не найдена"

    story = videopage.story()
    assert story is not None,"Сюжеты не найдены"