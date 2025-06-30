from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class DetalStory:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 15)
        self.original_window = None

    def open_detal_story(self):
        self.browser.get('https://www.sport-express.ru/football/rus_cup/stories/kubok-rossii-pley-off-puti-rpl-i-regionov-1-4-finala-1-2-i-final-zherebevka-pary-i-rezultaty-matchey-2023-2024-2140252/')

    def menu_nadlogo(self):
        try:
            menu_nadlogo = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')))
            logging.info("Меню найдено")
            return menu_nadlogo
        except TimeoutException:
            return None


    def h1(self):
        try:
            h1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//h1[contains(text(),'Кубок России: плей-офф и финалы пути РПЛ и пути ре')]")))
            logging.info("Заголовок найден")
            return h1
        except TimeoutException:
            return None

    def social(self):
        try:
            social = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='se-material-page__social']")))
            logging.info("Лайки и дизлайки найдены")
            return social
        except TimeoutException:
            return None

    def material(self,expected_count=16):
        try:
            material = self.wait.until(
                EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='clearfix icon_flag']")))
            actual_count = len(material)
            if actual_count == expected_count:
                logging.info(f"Найдено {actual_count} статей (ожидалось {expected_count})")
                return True
            else:
                logging.warning(f"Кол-во статей:{actual_count} (ожидалось {expected_count})")
                return False
        except TimeoutException:
            logging.error("Не удалось загрузить список статей")
            return False

    def reviews(self):
        try:
            reviews = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//h3[contains(text(),'Статьи')]")))
            logging.info("Блок статьи найден")
            return reviews
        except TimeoutException:
            return None

    def click_reviews(self,expected_count=22):
        try:
            click_reviews = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//body/div[@class='se-page-wrapper']/section[@class='se-page-content se-center-wrapper']/div[@class='se-page-content__inner']/div[@class='se-grid2col']/div[@class='se-grid2col__left']/div[@class='se-material-page']/div[@class='se-material-page__footer']/div[@class='se-material-page__footer-stories']/div[1]/section[1]/div[2]/a[1]")))
            click_reviews.click()

            material = self.wait.until(
                EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='clearfix icon_flag']")))
            actual_count = len(material)
            if actual_count == expected_count:
                logging.info(f"Найдено {actual_count} статей (ожидалось {expected_count})")
                return True
            else:
                logging.warning(f"Кол-во статей:{actual_count} (ожидалось {expected_count})")
                return False
        except TimeoutException:
            logging.error("Не удалось загрузить список статей")
            return False

    def news(self):
        try:
            news = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//h3[contains(text(),'Новости')]")))
            logging.info("Блок новости найден")
            return news
        except TimeoutException:
            return None

    def click_news(self,expected_count=24):
        try:
            click_news = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//body/div[@class='se-page-wrapper']/section[@class='se-page-content se-center-wrapper']/div[@class='se-page-content__inner']/div[@class='se-grid2col']/div[@class='se-grid2col__left']/div[@class='se-material-page']/div[@class='se-material-page__footer']/div[@class='se-material-page__footer-stories']/div[2]/section[1]/div[2]/a[1]")))
            click_news.click()

            material = self.wait.until(
                EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='se19-news-item mr_35']")))
            actual_count = len(material)
            if actual_count == expected_count:
                logging.info(f"Найдено {actual_count} статей (ожидалось {expected_count})")
                return True
            else:
                logging.warning(f"Кол-во статей:{actual_count} (ожидалось {expected_count})")
                return False
        except TimeoutException:
            logging.error("Не удалось загрузить список статей")
            return False

    def video(self):
        try:
            video = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//h3[contains(text(),'Видео')]")))
            logging.info("Блок видео найден")
            return video
        except TimeoutException:
            return None

    def click_video(self,expected_count=34):
        try:
            click_video = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//body/div[@class='se-page-wrapper']/section[@class='se-page-content se-center-wrapper']/div[@class='se-page-content__inner']/div[@class='se-grid2col']/div[@class='se-grid2col__left']/div[@class='se-material-page']/div[@class='se-material-page__footer']/div[@class='se-material-page__footer-stories']/div[3]/section[1]/div[2]/a[1]")))
            click_video.click()

            material = self.wait.until(
                EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='clearfix icon_flag']")))
            actual_count = len(material)
            if actual_count == expected_count:
                logging.info(f"Найдено {actual_count} статей (ожидалось {expected_count})")
                return True
            else:
                logging.warning(f"Кол-во статей:{actual_count} (ожидалось {expected_count})")
                return False
        except TimeoutException:
            logging.error("Не удалось загрузить список статей")
            return False

    def photo(self):
        try:
            photo = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//h3[contains(text(),'Фото')]")))
            logging.info("Блок фото найден")
            return photo
        except TimeoutException:
            return None

    def click_photo(self,expected_count=44):
        try:
            click_photo = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//body/div[@class='se-page-wrapper']/section[@class='se-page-content se-center-wrapper']/div[@class='se-page-content__inner']/div[@class='se-grid2col']/div[@class='se-grid2col__left']/div[@class='se-material-page']/div[@class='se-material-page__footer']/div[@class='se-material-page__footer-stories']/div[4]/section[1]/div[2]/a[1]")))
            click_photo.click()

            material = self.wait.until(
                EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='clearfix icon_flag']")))
            actual_count = len(material)
            if actual_count == expected_count:
                logging.info(f"Найдено {actual_count} статей (ожидалось {expected_count})")
                return True
            else:
                logging.warning(f"Кол-во статей:{actual_count} (ожидалось {expected_count})")
                return False
        except TimeoutException:
            logging.error("Не удалось загрузить список статей")
            return False

    def calend(self):
        try:
            calen = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Календарь')]")))
            logging.info("Календарь найден")
            calen.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/football/L/russia/cup/2024-2025/calendar/tours/', "Не правильный урл календаря"
            return calen
        except TimeoutException:
            return None