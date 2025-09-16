from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.description("Тестирование поля поиска по автору на сайте Читай-город.")
class SearchByAuthor:
    """Класс для выполнения поиска книг по автору на сайте Читай-город."""

    def __init__(self, author_name: str):
        """
        Инициализация класса SearchByAuthor.

        :param author_name: Имя автора, книги которого необходимо найти.
        """
        self.author_name = author_name

    @allure.step("Поиск книги по автору")
    def search_by_author(self, driver: webdriver.Chrome) -> None:
        """
        Поиск книг по имени автора на сайте Читай-город.

        :param driver: Экземпляр драйвера Selenium (в данном случае Chrome).
        :raises Exception: Возникает, если не удается найти элементы поиска на странице.
        """
        try:
            # Ввод имени автора в строку поиска
            search_input = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "search"))
            )
            search_input.clear()
            search_input.send_keys(self.author_name)

            # Клик по кнопке поиска
            search_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "search-form__button-search"))
            )
            search_button.click()

        except Exception as e:
            allure.attach(str(e), name="error", attachment_type=allure.attachment_type.TEXT)
            raise