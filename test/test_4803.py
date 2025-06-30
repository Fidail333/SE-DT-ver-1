from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.nhltable import NhlTable



def test_nhltable(browser):
    nhltable = NhlTable(browser)
    nhltable.open()
    nhltable.menu_nad_logo()
    nhltable.tablo()
    nhltable.podval()
    nhltable.plitka_glavn()
    nhltable.poll()
    nhltable.glavn_news()
    nhltable.news()
    nhltable.reviews()
    nhltable.video()
    nhltable.table()
    nhltable.h1()
    nhltable.conference()
