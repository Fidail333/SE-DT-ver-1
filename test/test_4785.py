from pages.tagcomands import TagComand



def test_tagcomand(browser):
    tagcomand = TagComand(browser)
    tagcomand.open()

    menu = tagcomand.menu()
    assert menu is not None, "Меню не найдено"

    proverka = tagcomand.verify_all_elements()
    assert proverka, "Найдены не все элементы"

    tagcomand.news()
    assert tagcomand.news(expected_count=30), "Не правильное кол-во новостей"

    click_rev = tagcomand.reviews()
    assert click_rev is not None, "Не была нажата кнопка(статьи)"

    tagcomand.reviews_len()
    assert tagcomand.reviews_len(expected_count=30)

    click_photo = tagcomand.photo()
    assert click_photo is not None, "Кнопка не была найдена(фото)"

    tagcomand.photo_len()
    assert tagcomand.photo_len(expected_count=30)

    click_video = tagcomand.video()
    assert click_video is not None, "Кнопка не была найдена(видео)"

    tagcomand.video_len()
    assert tagcomand.video_len(expected_count=30)

    sostav = tagcomand.sostav()
    assert sostav is not None, 'Кнопка состава не была найдена(или не выполнены другие действия)'

    raspis = tagcomand.rasposanie()
    assert raspis is not None, "Кнопка расписания не была найдена(или не выполнены другие действия)"

    stat = tagcomand.stat()
    assert stat is not None, "Кнопка статистики не найдена(или не выполнены другие действия)"

    player_stat = tagcomand.player_stat()
    assert player_stat is not None, "Выполняемые действия - провалены"

    comand_stat = tagcomand.stat_comand()
    assert comand_stat is not None, "Статистика команды - ошибка"

    treners = tagcomand.treners()
    assert treners is not None, "Тренера не найдены или ошибка"

    soperniki = tagcomand.apponents()
    assert soperniki is not None, "Соперники - ошибка"