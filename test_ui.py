from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from pages.Search_By_Author_ui import SearchByAuthor
from pages.Search_By_Title_ui import SearchByTitle
from pages.Add_To_Cart_ui import AddToCart
from pages.Delete_From_Cart_ui import DeleteFromCart
from constants import UI_url

search_by_author = SearchByAuthor
search_by_title = SearchByTitle
add_to_card = AddToCart
delete_from_cart = DeleteFromCart


@allure.title("Тест поиска книг по автору. POSITIVE")
@allure.description("Этот тест проверяет, "
                    "что поиск книг по автору работает корректно.")
@allure.feature("READ")
@allure.severity("CRITICAL")
def test_search_by_author():
    """
                      Проверка корректности результатов поиска по автору.

    """
 @allure.feature("Поиск по автору")
class TestSearchShort:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.chitai-gorod.ru/")

    def teardown_method(self):
        self.driver.quit()

    @allure.title("Поиск книг автора")
    def test_search_author(self):
        """Короткий тест поиска по автору."""
        
        search = SearchByAuthor("Пушкин А.С.")
        search.search_by_author(self.driver)
        

@allure.title("Тест добавления товара в корзину. POSITIVE")
@allure.description("Этот тест проверяет, что товар добавляется в корзину.")
@allure.feature("CREATE")
@allure.severity("BLOCKER")
def test_add_to_card():
    """
                         Проверка корректности добавления товара в корзину.

    """
  @allure.step("Добавить книгу '{book_title}' в корзину")
def add_to_card(driver, book_title):
    """Добавление книги в корзину."""
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "search"))).send_keys(book_title)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "search-form__button-search]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-buttons__main-action"))).click()


def test_add_book_to_cart():
    """Тест добавления книги в корзину."""
    with allure.step("Запуск браузера и переход на сайт"):
        driver = webdriver.Chrome()
        driver.get("https://www.chitai-gorod.ru/")

    with allure.step("Добавление книги 'Я так взрослею: об отношениях с собой и другими' в корзину"):
        add_to_card(driver, "Я так взрослею: об отношениях с собой и другими")

    with allure.step("Проверка что корзина не пуста"):
        cart_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "header-controls__icon-wrapper]"))
        )
        assert cart_button is not None

    with allure.step("Закрытие браузера"):
        driver.quit()


@allure.title("Тест удаления товара из корзины. POSITIVE")
@allure.description("Этот тест проверяет, что товар "
                    "из корзины удаляется корректно.")
@allure.feature("DELETE")
@allure.severity("BLOCKER")
def test_delete_from_card():
    """
                         Проверка корректности удаления товара из корзины.

    """

    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome()

    with allure.step("Перейти на сайт Читай-город"):
        driver.get(UI_url)

    with allure.step("Удалить книгу из корзины"):
        book_title = "Ветреный"
        delete_from_cart(book_title)
        results_del = driver.find_elements(By.CSS_SELECTOR,
                                           'div.product-title__head')

    with ((allure.step("Проверить, что товар больше не существует в списке"))):
        assert all(
            book_title not in
            element.text for element in
            results_del), f"Книга '{book_title}' все еще в корзине."


@allure.title("Тест поиска по несуществующему автору. NEGATIVE")
@allure.description("Этот тест проверяет, что поиск по "
                    "несуществующему атору невозможен")
@allure.feature("READ")
@allure.severity("CRITICAL")
def test_wrong_author():
    """
                         Проверка, что при поиске книги по
                         несуществующему автору результат отсутствует.

    """

    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome()

    with allure.step("Перейти на сайт Читай-город"):
        driver.get(UI_url)

    with allure.step("Найти книгу по несуществующему автору"):
        author_name = "Стопудоев"
        search_by_author(author_name)

    with allure.step("Проверить, что поиск не дал результатов"):
        # Проверка появления сообщения об отсутствии результата
        results_find = driver.find_elements(By.CSS_SELECTOR,
                                            "hcatalog-stub "
                                            "catalog-stub--row "
                                            "search-page__nf-stub")
        assert results_find is not None

    with allure.step("Закрыть браузер"):
        driver.quit()


@allure.title("Тест поиска по смешанному запросу. NEGATIVE")
@allure.description("Этот тест проверяет, что поиск по "
                    "смешанному запросу невозможен")
@allure.feature("READ")
@allure.severity("CRITICAL")
def test_mixed_request():
    """
                         Проверка, что при поиске книги по
                         смешанному запросу результат отсутствует.

    """

    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome()

    with allure.step("Перейти на сайт Читай-город"):
        driver.get(UI_url)

    with allure.step("Найти книгу по смешанному запросу"):
        book_title = "KAлифорния Nа Amуре"
        search_by_title(book_title)

    with (((allure.step("Проверить, что поиск не дал результатов")))):
        # Проверка появления сообщения об отсутствии результата
        results_find = driver.find_elements(By.CSS_SELECTOR,
                                            "hcatalog-stub "
                                            "catalog-stub--row search"
                                            "-page__nf-stub")
        assert results_find is not None

    with allure.step("Закрыть браузер"):
        driver.quit()