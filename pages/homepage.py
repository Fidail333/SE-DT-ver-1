from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
import time

class HomePage:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.original_window = None

    def open(self):
        self.browser.get('https://www.sport-express.ru/')
        sleep(6)

    def tablo_find(self):
       try:
           tablo_find = self.wait.until(
               EC.visibility_of_element_located((By.XPATH,"//div[@class='se-translation-scoreboard__control']")))
           logging.info("Табло найдено и видимо!")
           return tablo_find
       except TimeoutException:
           logging.error("Блок не найден")
           return None

    def plitka(self):
        try:
            plitka = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='se-top-materials-with-photo']")))
            logging.info("Плитка найдена")
            return plitka
        except TimeoutException:
            return None


    def news(self):
        try:
            news = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Новости')]")))
            logging.info(" Блок с новостями найден и видим!")
            return news
        except TimeoutException:
            return None

    def check_metrika_console_events(self):
        try:
            time.sleep(5)
            logs = self.browser.get_log('browser')
            logging.info(f"Всего логов в консоли: {len(logs)}")

            if not logs:
                logging.error("Консоль браузера пуста!")
                assert False, "Нет логов в консоли браузера"

            target_patterns = [
                "view_main_page_tablo_betcity",
                "view_main_page_tablo_fonbet",
                "view_main_page_tablo_betboom",
                "view_main_page_tablo_winline"
            ]

            found = False
            for log in logs:
                message = log.get('message', '')
                if any(target in message for target in target_patterns):
                    logging.info(f"Найдено событие Метрики: {message[:300]}...")
                    found = True
                    break

            if not found:
                logging.error("Нужные события не найдены. Последние логи:")
                for log in logs[-5:]:
                    logging.error(f"➜ {log.get('message', '')[:200]}...")
                assert False, "События Метрики не найдены в консоли"
            return True
        except Exception as e:
            logging.error(f"Ошибка при проверке консоли: {str(e)}")
            assert False, f"Ошибка проверки консоли: {str(e)}"

    def main_news(self):
            try:
                main_news = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Главные новости')]")))
                logging.info("Главные новости видны и найдены!")
                main_news.click()
                assert self.browser.current_url == 'https://www.sport-express.ru/news/?isEditorialChoice=1', "Не правильная ссылка блока главные новости"
                self.browser.back()
                return main_news
            except TimeoutException:
                return None

    def block_video(self):
        try:
            for _ in range(20):
                try:
                    block_video = self.browser.find_element(By.XPATH,"//div[@class='se-titled-block']")
                    logging.info("Блок найден и виден")
                    return block_video
                except:
                    self.browser.execute_script("window.scrollBy(0, 500);")
            logging.info("Блок не найден после прокрутки")
            return None
        except TimeoutException:
            return None

    def click_video(self):
        try:
            click_video = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[@class='se-link se-link--arrow-right'][contains(text(),'Больше видео')]")))
            logging.info("Кнопка найдена и видна!")
            click_video.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/videoreports/', "Не правильная ссылка кнопка больше видео"
            self.browser.back()
            return click_video
        except TimeoutException:
            return None


    def block_reviews(self):
        try:
            for _ in range(20):
                try:
                    block_reviews = self.browser.find_element(By.XPATH,"//div[contains(text(),'Статьи')]")
                    logging.info("Блок статьи найден и виден")
                    return block_reviews
                except:
                    self.browser.execute_script("window.scrollBy(0, 500);")
            logging.info("Блок статьи не найден после прокрутки")
            return None
        except TimeoutException:
            return None

    def read(self):
        try:
            read = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='se-readers-choice se-readers-choice--theme-main']")))
            logging.info("Блок выбор читателей найден")
            return read
        except  TimeoutException:
            return None


    def block_photo(self):
        try:
            block_photo = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Новые альбомы')]")))
            logging.info("Блок с фото найден и видим")
            block_photo.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/photoreports/', "Не правильная ссылка все фото"
            self.browser.back()
            return block_photo
        except TimeoutException:
            return None

    def block_reklama(self):
        try:
            for _ in range(20):
                try:
                    block_reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")
                    logging.info("Блок с рекламой найден и видим")
                    return block_reklama
                except:
                    self.browser.execute_script("window.scrollBy(0, 500);")
            logging.info("Блок с рекламой не найден после прокрутки")
            return None
        except TimeoutException:
            return None

    def block_table(self):
        try:
            block_table = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Все результаты / календарь')]")))
            logging.info("Блок с положением команд найден и видим")
            block_table.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/football/L/russia/premier/2025-2026/calendar/tours/', "Не правильная ссылка положения команд"
            self.browser.back()
            return block_table
        except TimeoutException:
            return None

    def block_stat(self):
        try:
            for _ in range(20):
                try:
                   block_stat = self.browser.find_element(By.XPATH,"//div[@class='se-tab-panel se-tab-panel--active ']//div[@class='se-statblock-leaders__content']//div//a[@class='se-button'][contains(text(),'Вся статистика')]")
                   logging.info("Блок со статистикой найден и видим")
                   block_stat.click()
                   assert self.browser.current_url == 'https://www.sport-express.ru/football/L/russia/premier/2025-2026/statistics/bombardiers/', "Не правильная ссылка статистики"
                   self.browser.back()
                   return block_stat
                except:
                    self.browser.execute_script("window.scrollBy(0, 500);")
            logging.error("Блок не найден после прокрутки")
            return None
        except TimeoutException:
            return None


