from itertools import count

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FigurkaNew:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 15)  # Инициализация ожидания

    def open(self):
        self.browser.get('https://www.sport-express.ru/winter/figure-skating/grand-pri/2022-2023/calendar/')
        # Ждем загрузки ключевого элемента вместо sleep
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='se-page-filters']")
        ))

    def apply_skate_america_filter(self):
        # Открываем фильтр
        itap = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='se-select__value-container']")
        ))
        itap.click()

        # Выбираем опцию
        america = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(text(),'Skate America')]")
        ))
        america.click()

        # Ждем обновления данных
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='se-competition-titled-block__title' and contains(., 'Skate America')]")
        ))

    def navigate_to_athletes(self):
        sports_link = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'se-page-menu-item') and contains(text(), 'Спортсмены')]")
        ))
        sports_link.click()

        # Проверяем URL с ожиданием
        self.wait.until(EC.url_to_be(
            'https://www.sport-express.ru/winter/figure-skating/grand-pri/2022-2023/players/'
        ))

    def verify_athletes_page(self):
        # Проверяем заголовок
        assert "Спортсмены" in self.browser.find_element(
            By.XPATH, "//div[@class='sp-sport-page__title']"
        ).text

        # Проверяем наличие секций
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(),'ДР')]")
        ))
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(),'Рост')]")
        ))

    def verify_flag_count(self, count):
        flags = self.wait.until(EC.visibility_of_all_elements_located(
            (By.XPATH, "//div[@class='se-file-image se-file-image--circle sp-competition-players-list__country-flag']")
        ))
        assert len(flags) == count, f"Ожидалось {count} флагов, найдено {len(flags)}"

    def select_germany(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='se-select__value']")
        )).click()

        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'se-select__item') and contains(., 'Германия')]")
        )).click()

    def verify_athlete_count(self, count):
        athletes = self.wait.until(EC.visibility_of_all_elements_located(
            (By.XPATH, "//td[@class='se-advanced-table-cell se-advanced-table-cell--sorted']")
        ))
        assert len(athletes) == count, f"Ожидалось {count} спортсменов, найдено {len(athletes)}"














