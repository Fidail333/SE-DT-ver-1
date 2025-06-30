import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
from selenium.common.exceptions import NoSuchElementException


class TagComand:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.original_window = None

    def open(self):
        self.browser.get('https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/')

    def menu(self):
        try:
            menu = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='se-menu-subtop se-menu-subtop--breadcrumb']")))
            logging.info("Меню найдено")
            return menu
        except TimeoutException:
            return None

    def verify_all_elements(self):
        elements = [
            ("//div[@class='sp-param-list__cols']//div[1]//div[1]//div[1]", "Страна"),
            ("//div[@class='sp-param-list__cols']//div[1]//div[2]//div[1]", "Арена"),
            ("//div[@class='sp-param-list__cols']//div[1]//div[3]//div[1]", "Тренер"),
            ("//div[contains(text(),'Восточная')]", "Конф"),
            ("//div[contains(text(),'Дивизион Харламова')]","Дивизион"),
            ("//div[normalize-space()='http://www.metallurg.ru/']", "сайт")
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

    def news(self, expected_count=30):
        try:
            news = self.wait.until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, "//div[@class='se-tag-profile-material-list__item']")))
            actual_count = len(news)
            if actual_count == expected_count:
                logging.info(f"Найдено {actual_count} новостей (ожидалось {expected_count})")
                return True
            else:
                logging.warning(f"Кол-во новостей:{actual_count} (ожидалось {expected_count})")
                return False
        except TimeoutException:
            logging.error("Не удалось загрузить новостей")
            return False


    def reviews(self):
        try:
            click = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[@class='se-button se-button--rounded se-tag-profile-materials-filter__bottom'][contains(text(),'Статьи')]")))
            logging.info("Кнопка найдена")
            click.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/reviews/', "Не правильный урл статей"
            return click
        except TimeoutException:
            return None

    def reviews_len(self,expected_count=30):
        try:
            reviews = self.wait.until(
                EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='se-tag-profile-material-list__item']")))
            actual_count = len(reviews)
            if actual_count == expected_count:
                logging.info(f"Найдено {actual_count} статей ожидалось {expected_count}")
                return True
            else:
                logging.warning(f"Кол-во статей:{actual_count} ожидалось {expected_count}")
                return False
        except TimeoutException:
            logging.error("Не удалось загрузить статьи")
            return False


    def photo(self):
        try:
            click = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[@class='se-button se-button--rounded se-tag-profile-materials-filter__bottom'][contains(text(),'Фото')]")))
            logging.info("Кнопка найдена")
            click.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/photoreports/', "Не правильный урл фото"
            return click
        except TimeoutException:
            return None

    def photo_len(self,expected_count=30):
        try:
            photo = self.wait.until(
                EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='se-tag-profile-material-list__item']")))
            actual_count = len(photo)
            if actual_count == expected_count:
                logging.info(f"Найдено {actual_count} фото ожидалось {expected_count})")
                return True
            else:
                logging.warning(f"Кол-во фото:{actual_count} ожидалось {expected_count})")
                return False
        except TimeoutException:
            logging.error("Не удалось загрузить статьи")
            return False


    def video(self):
        try:
            click = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[@class='se-button se-button--rounded se-tag-profile-materials-filter__bottom'][contains(text(),'Видео')]")))
            logging.info("Кнопка найдена")
            click.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/videoreports/', "Не правильный урл видео"
            return click
        except TimeoutException:
            return None

    def video_len(self,expected_count=30):
        try:
            photo = self.wait.until(
                EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='se-tag-profile-material-list__item']")))
            actual_count = len(photo)
            if actual_count == expected_count:
                logging.info(f"Найдено {actual_count} видео ожидалось {expected_count})")
                return True
            else:
                logging.warning(f"Кол-во видео:{actual_count} ожидалось {expected_count})")
                return False
        except TimeoutException:
            logging.error("Не удалось загрузить статьи")
            return False

    def sostav(self):
        try:
            click = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Состав')]")))
            logging.info("Кнопка состава найдена и видна")
            click.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/players/', "Не правильный урл состава"

            click2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//body[1]/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[4]/a[1]")))
            logging.info("Игрок найден")
            click2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/player/14283/', "Не правильный урл игрока"
            self.browser.back()
            return click2
        except TimeoutException:
            return None

    def rasposanie(self):
        try:
            click = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Расписание')]")))
            logging.info("Кнопка расписание найдена и видна")
            click.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/schedule/', "Не правильный урл расписания"

            click2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//tbody/tr[4]/td[7]/a[1]")))
            logging.info("матч найден")
            click2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/matchcenter/116907/#protocol', "Не правильный урл матча"
            self.browser.back()
            return click2
        except TimeoutException:
            return None

    def stat(self):
        try:
            click = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Статистика игроков')]")))
            logging.info("Кнопка cтатистика найдена и видна")
            click.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/players-stats/', "Не правильный урл статистики"

            click2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//img[@title='Михайлис Никита']")))
            logging.info("Игрок найден")
            click2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/nikita-mihaylis-15180/', "Не правильный урл игрока"
            self.browser.back()
            return click2
        except TimeoutException:
            return None


    def player_stat(self):
        try:
            click1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'Полевые игроки')]")))
            logging.info("Кнопка полевые игроки найдена")
            click1.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/players-stats/?stage=undefined&role=outfields',"Не правильный урл полевые игроки"

            click2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//img[@title='Канцеров Роман']")))
            logging.info("Полевой игрок найден")
            click2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/player/15809/', "Не правильный урл игрока пол"
            self.browser.back()

            click3 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'Вратари')]")))
            logging.info("Вратари найдены")
            click3.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/players-stats/?stage=undefined&role=goalkeeper', "Не правильный урл вратарей"

            click4 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//img[@title='Смолин Александр']")))
            logging.info("Игрок вратарь найден")
            click4.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/player/16375/', "Не правильный урл вратаря"
            self.browser.back()

            click5 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Защитники')]")))
            logging.info("Кнопка защитники найдена")
            click5.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/players-stats/?stage=undefined&role=defense', "Не правильный защитников"

            click6 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//img[@title='Пресс Робин']")))
            logging.info(" защитники найдена")
            click6.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/player/14673/', "Не правильный защитника урл"
            self.browser.back()

            click7 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Нападающие')]")))
            logging.info("Кнопка нападающие найдена")
            click7.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/players-stats/?stage=undefined&role=forward', "Не правильный урл нападающих"

            click6 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//img[@title='Силантьев Дмитрий']")))
            logging.info(" защитники найдена")
            click6.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/dmitriy-silantev-30291/', "Не правильный нападающего урл"
            self.browser.back()
            return click6
        except TimeoutException:
            return None

    def stat_comand(self):
        try:
            click = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Статистика команды')]")))
            logging.info("Кнопка cтатистика_команды найдена и видна")
            click.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/stats/', "Не правильный урл статистики_команды"

            click2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//tbody/tr[1]/td[2]/div[1]/div[1]")))
            click2.click()
            logging.info("Турнир раскрыт")
            time.sleep(1)

            click3 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//tbody/tr[1]/td[2]/div[1]/a[2]")))
            logging.info("Команда найдена")
            click3.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/lokomotiv-yar-33/', "Не правильный урл команды"
            self.browser.back()
            return click3
        except TimeoutException:
            return None

    def treners(self):
        try:
            click = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Тренеры')]")))
            logging.info("Кнопка тренеры найдена и видна")
            click.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/trainers/', "Не правильный урл тренеров"

            click2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//img[@title='Кинэн Майк']")))
            logging.info("Игрок найден")
            click2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/trainer/58/', "Не правильный урл тренера"
            self.browser.back()
            return click2
        except TimeoutException:
            return None


    def apponents(self):
        try:
            click = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Соперники')]")))
            logging.info("Кнопка соперники найдена и видна")
            click.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/competitor/', "Не правильный урл соперников"

            click2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Адмирал')]")))
            logging.info("Игрок найден")
            click2.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/tag/admiral-11093/?page=', "Не правильный урл тега соперника"
            return click2
        except TimeoutException:
            return None