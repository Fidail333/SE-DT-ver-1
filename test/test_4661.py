import logging
from pages.newspaperpage import PaperGazeta

def test_newspapers(browser):
    newspaperspage = PaperGazeta(browser)
    newspaperspage.open_gazeta()

    reklama = newspaperspage.reklama()
    if reklama is None:
        logging.warning("Реклама не выводится, это норма")
    else:
        logging.info("Реклама выводится")

    btn_calend = newspaperspage.calendar()
    assert btn_calend is not None,"Кнопка календаря не найдена"

    proverka = newspaperspage.proverka()
    assert proverka is not None,"Календарь не отображается"