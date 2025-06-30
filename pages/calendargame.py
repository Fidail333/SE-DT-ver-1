from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class CalendarGame:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.original_window = None


    def open(self):
        self.browser.get('https://www.sport-express.ru/football/L/russia/premier/2024-2025/calendar/tours/')

    def h1(self):
        try:
            h1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//h1[contains(text(),'Россия. Премьер-лига 2024-2025, расписание матчей,')]")))
            logging.info("Заголовок найден")
            return h1
        except TimeoutException:
            return None

    def check_metrika_console_events(self):
        try:
            sleep(5)
            logs = self.browser.get_log('browser')
            logging.info(f"Всего логов в консоли: {len(logs)}")

            if not logs:
                logging.error("Консоль браузера пуста!")
                assert False, "Нет логов в консоли браузера"

            target_patterns = [
                "view_calendar_betcity",
                "view_calendar_fonbet",
                "view_calendar_betboom",
                "view_calendar_winline"
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

    def click_and_check_metrika_events(self):
        try:
            sleep(5)
            elements_to_click = {
                "//div[@data-component='bookie-badge']//img": [
                    "click_calendar_winline",
                    "click_calendar_fonbet",
                    "click_calendar_betboom",
                    "click_calendar_betcity"
                ]
            }

            results = {}
            main_window = self.browser.current_window_handle

            for xpath, expected_patterns in elements_to_click.items():
                try:

                    self.browser.find_element(By.XPATH, xpath).click()
                    logging.info(f"Выполнен клик по элементу: {xpath}")
                    sleep(2)


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


    def match(self):
        try:
            match = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//tbody/tr[8]/td[3]/div[1]/p[1]/a[1]")))
            logging.info("Счет матча найден")
            match.click()
            assert self.browser.current_url == 'https://www.sport-express.ru/football/rfpl/fbl_match-himki-dinamo-mh-397434/', "Не правильный матч"
            self.browser.back()
            return match
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