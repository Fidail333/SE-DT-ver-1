
from pages.storypage import StoryPage

def test_storypage(browser):
    storypage = StoryPage(browser)
    storypage.open_story()

    story = storypage.h1_story()
    assert story is not None, "Заголовок не найден"

    basket = storypage.baskt()
    assert basket is not None,"Баскетбол не найден"

    page = storypage.next_page()
    assert page is not None, "Следующая страница не найдена"