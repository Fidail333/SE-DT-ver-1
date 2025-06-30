from itertools import count

from selenium.webdriver.common.by import By
from time import sleep

class Reklama:

    def __init__(self, browser):
        self.browser = browser


    def open(self):
        self.browser.get('https://www.sport-express.ru/advert/www/')
        sleep(6)

    def everest(self):
        everest = self.browser.find_element(By.XPATH,"(//h2[@class='redline pt_10 fs_21'])[1]")

    def click_verest(self):
        click_verest = self.browser.find_element(By.XPATH,"//a[contains(text(),'ЭВЕРЕСТ')]")
        click_verest.click()
        assert self.browser.current_url == 'https://www.everest-sales.ru/', "Не правильная ссылка эвеерста"
        self.browser.back()

    def autor(self):
        autor = self.browser.find_element(By.XPATH,"//a[@class='se-staticpage-menu-group__row-item'][contains(text(),'Редакция и авторы')]")
        autor.click()
        sleep(5)
        assert self.browser.current_url == 'https://www.sport-express.ru/editorial/', "Не правлиьный урл авторов"

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Редакция')]")

    def glv(self):
        glv = self.browser.find_element(By.XPATH,"//a[contains(text(),'Максим Максимов')]")

    def spisok(self,count):
        spisok = self.browser.find_elements(By.XPATH,"//div[@class='se-author-list__item']")
        assert len(spisok) == count
        sleep(2)

    def knopka(self):
        knopka = self.browser.find_element(By.XPATH, "(//div[@class='se-button se-button--white se-button--size-big'][contains(text(),'Показать еще')])[1]")
        knopka.click()
        sleep(2)

    def spisok2(self,count):
        spisok2 = self.browser.find_elements(By.XPATH,"//div[@class='se-author-list__item']")
        assert len(spisok2) == count

    def perexod(self):
        perexod = self.browser.find_element(By.XPATH,"//a[contains(text(),'Марат Сафин')]")
        perexod.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/author/marat-safin/', "не правильный автор"

