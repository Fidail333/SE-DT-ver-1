from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class McFootball:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.original_window = None

    def open(self):
        self.browser.get('https://www.sport-express.ru/live/football/')

    def reklama(self):
        try:
            reklama = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@id='adfox_15645683733586888']")))
            logging.info("Реклама найдена")
            return reklama
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

    def click_and_check_metrika_events(self):
        try:
            sleep(5)
            elements_to_click = {
                "//div[@data-component='bookie-badge']//img": [
                    "click_matchcentr_winline",
                    "click_matchcentr_fonbet",
                    "click_matchcentr_betboom",
                    "click_matchcentr_betcity"
                ]
            }

            results = {}
            main_window = self.browser.current_window_handle  # Запоминаем основное окно

            for xpath, expected_patterns in elements_to_click.items():
                try:
                    # Кликаем по элементу (это откроет новое окно)
                    self.browser.find_element(By.XPATH, xpath).click()
                    logging.info(f"Выполнен клик по элементу: {xpath}")
                    sleep(2)

                    # Переключаемся обратно на основное окно
                    self.browser.switch_to.window(main_window)

                    logs = self.browser.get_log('browser')
                    logging.info(f"Всего логов в консоли после клика {xpath}: {len(logs)}")

                    found = False
                    for log in logs:
                        message = log.get('message', '')
                        if any(pattern in message for pattern in expected_patterns):
                            logging.info(f"Найдено событие Метрики: {message[:300]}...")
                            found = True
                            break

                    results[xpath] = found

                    if not found:
                        logging.error(f"События {expected_patterns} не найдены после клика {xpath}. Последние логи:")
                        for log in logs[-5:]:
                            logging.error(f"➜ {log.get('message', '')[:200]}...")

                except Exception as e:
                    logging.error(f"Ошибка при клике/проверке для элемента {xpath}: {str(e)}")
                    results[xpath] = False
                    # В случае ошибки убедимся, что вернулись в основное окно
                    self.browser.switch_to.window(main_window)

            if not all(results.values()):
                failed = [xpath for xpath, success in results.items() if not success]
                assert False, f"События Метрики не найдены после кликов по: {', '.join(failed)}"

            return True

        except Exception as e:
            logging.error(f"Ошибка при проверке консоли: {str(e)}")
            assert False, f"Ошибка проверки консоли: {str(e)}"
    def check_metrika_console_events(self):
        try:
            sleep(5)
            logs = self.browser.get_log('browser')
            logging.info(f"Всего логов в консоли: {len(logs)}")

            if not logs:
                logging.error("Консоль браузера пуста!")
                assert False, "Нет логов в консоли браузера"

            target_patterns = [
                "view_matchcentr_betcity",
                "view_matchcentr_fonbet",
                "view_matchcentr_betboom",
                "view_matchcentr_winline"
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

    def buttons(self):
        button = [
            "//a[contains(text(),'Сегодня')]",
            "//a[contains(text(),'Завтра')]",
            "//a[contains(text(),'Вчера')]",
        ]

        for xpath in button:
            try:
                self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            except TimeoutException:
                logging.warning(f"Рекламный блок не найден: {xpath}")
                return None

        logging.info("Все кнопки найдены")
        return True

    def data_calend(self):
        try:
            calend1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//button[@class='react-date-picker__calendar-button react-date-picker__button']")))
            logging.info("Кнопка календаря найдена")
            calend1.click()

            calend2 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='react-calendar']")))
            logging.info("Календарь найден и виден")
            return calend2
        except TimeoutException:
            return None

    def footer(self):
        try:
            footer = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//footer[@class='se-footer']")))
            logging.info("Подвал найден")
            return footer
        except TimeoutException:
            return None

    def selector(self):
        try:
            select = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@class='se-sport-navigator__sport']")))
            logging.info("Селектор найден")
            select.click()

            click = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@id='react-select-sports-option-0-5']//div[1]")))
            logging.info("Кнопка меняю гандбол - найдена")
            click.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/live/handball/', "не правильный гандбол"
            return click
        except TimeoutException:
            return None