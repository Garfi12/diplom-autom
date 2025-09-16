from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


@allure.description("Тестирование добавления товара в корзину на сайте Читай-город.")
class AddToCart:

    # ИНИЦИАЛИЗАЦИЯ
    def __init__(self, book_title: str):
        """
        Создает объект для добавления книги в корзину.

        :param book_title: Название книги для добавления в корзину.
        """
        self.book_title = book_title

    # ПОИСК КНИГИ ПО НАЗВАНИЮ И ДОБАВЛЕНИЕ В КОРЗИНУ
    @allure.step("Поиск книги '{book_title}' и добавление в корзину")
    def search_by_title(self, driver: webdriver.Chrome, book_title: str) -> dict:
        """
        Ищет книгу по названию и добавляет её в корзину.

        :param driver: Экземпляр драйвера Selenium.
        :param book_title: Название книги для поиска.
        :return: Словарь с результатами поиска.
        """
        try:
            # Ввод названия книги в строку поиска
            driver.find_element(By.NAME, "search").send_keys(book_title)

            # Клик по кнопке поиска
            search_button_find = driver.find_element(By.CSS_SELECTOR, "search-form__button-search")
            search_button_find.click()

            # Клик по кнопке "Купить"
            search_button_buy = driver.find_element(By.CSS_SELECTOR, ".product-buttons__main-action")
            search_button_buy.click()

            # Открытие корзины
            cart_icon = driver.find_element(By.CSS_SELECTOR, ".header-controls__icon-wrapper")
            cart_icon.click()

            return {"status": "success", "book_title": book_title}

        except Exception as e:
            allure.attach(str(e), name="error", attachment_type=allure.attachment_type.TEXT)
            raise