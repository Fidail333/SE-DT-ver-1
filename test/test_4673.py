from pages.glavnfootball import GlavnFootball

def test_glavnnews(browser):
    glawnnews = GlavnFootball(browser)
    glawnnews.open()

    tablo = glawnnews.tablo_find()
    assert tablo is not None, "Табло не найдено"

    plitka = glawnnews.plitka()
    assert plitka is not None, "Плитка не найдена"

    news = glawnnews.news()
    assert news is not None, "Блок новостей не найден"

    glawnnews.check_metrika_console_events()

    main = glawnnews.main_news()
    assert main is not None, "Блок с главными новостями не найден"

    video = glawnnews.block_video()
    assert video is not None, "Блок с видео не найден"

    click = glawnnews.click_video()
    assert click is not None, "Клик для перехода в видео не прошел"

    reviews = glawnnews.block_reviews()
    assert reviews is not None, "Блок со статьями не найден"

    photo = glawnnews.block_photo()
    assert photo is not None, "Блок с фото не найден"

    reklama = glawnnews.block_reklama()
    assert reklama is not None, "Блок с рекламой не найден"

    #"poll = glawnnews.block_poll()
    #assert poll is not None, "Блок с опросами не найден"" временно отключил 30.06.2025 Фидаиль