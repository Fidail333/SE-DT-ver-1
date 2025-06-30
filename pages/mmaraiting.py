from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
from selenium.common.exceptions import NoSuchElementException



class MmaRaiting:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.original_window = None

    def open(self):
        self.browser.get('https://www.sport-express.ru/fighting/mma/ufc/2024/ratings/men/')

    def menu(self):
        try:
            menu = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')))
            logging.info("Меню найдено")
            return menu
        except TimeoutException:
            return None

    def h1(self):
        try:
            h1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='sp-sport-page__title']")))
            logging.info("Заголовок найден")
            return h1
        except TimeoutException:
            return None

    def boets(self, expected_count=15):
        try:
            player = self.wait.until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, "//div[@class='sp-ratings__fighter-info']")))
            actual_count = len(player)
            if actual_count == expected_count:
                logging.info(f"Найдено {actual_count} бойцов (ожидалось {expected_count})")
                return True
            else:
                logging.warning(f"Кол-во бойцов:{actual_count} (ожидалось {expected_count})")
                return False
        except TimeoutException:
            logging.error("Не удалось загрузить бойцов")
            return False

    def champion_panel(self):
        try:
            champion = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='se-fighter-champion-panel__left']")))
            logging.info("Панель чемпиона найдена")
            return champion
        except TimeoutException:
            return None

    def click_fighter(self):
        try:
            click1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Александр Пантожа')]")))
            logging.info("Чемпион найден")
            click1.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/aleksandr-pantozha-25211/', "Не правильный урл чемпиона"
            self.browser.back()

            click2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Брэндон Ройвал')]")))
            logging.info("Боец найден")
            click2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/brendon-royval-25214/', "Не правильный урл бойца"
            self.browser.back()
            return click2
        except TimeoutException:
            return None


    def verify_all_elements(self):
        elements = [
            ("//div[contains(@class,'asc')]", "Заголовок номер "),
            ("//div[contains(text(),'Боец')]", "Заголовок боец"),
            ("//div[contains(text(),'Рекорд в промоушене')]", "Рекорд"),
            ("//div[contains(text(),'Общий рекорд')]", "Общий рекорд")
        ]

        all_present = True

        for xpath, description in elements:
            try:
                self.browser.find_element(By.XPATH, xpath)
                logging.info(f"{description} - найден")
            except NoSuchElementException:
                logging.error(f"{description} - не найден")
                all_present = False

        return all_present

    def sort(self):
        try:
            sort1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[contains(@class,'asc')]")))
            logging.info("Кнопка номера найдена")
            sort1.click()

            sort2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[contains(@class,'sp-ratings__positions_number')][normalize-space()='1']")))
            logging.info("Сортировка работает")
            return sort2
        except TimeoutException:
            return None

    def select_aca(self):
        try:
            select = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='se-sport-navigator__competition']")))
            logging.info("Селектор переключения найден")
            select.click()

            select2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@id='react-select-competitions-option-0-4']")))
            logging.info("Нужный турнир найден")
            select2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/fighting/mma/aca/2025/calendar/', "Не правильный урл промоушена"

            select3 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='se-page-menu-item']//a[contains(text(),'Рейтинги')]")))
            logging.info("Кнопка рейтинги найдена")
            select3.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/fighting/mma/aca/2025/ratings/men/', "Не правильная ссылка рейтингов"
            return select3
        except TimeoutException:
            return None

    def reklama(self):
        try:
            reklama = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@id='adfox_15645683733586888']")))
            logging.info("Реклама найдена")
            return reklama
        except TimeoutException:
            return None