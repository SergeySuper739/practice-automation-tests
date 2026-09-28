import allure
from pages.modals_page import ModalsPage


@allure.feature("Modals")
class TestModals:

    @allure.title("Позитив: открытие Simple Modal")
    def test_open_simple(self, driver):
        page = ModalsPage(driver)
        page.open()
        page.open_simple_modal()
        assert page.is_modal_visible()

    @allure.title("Позитив: закрытие Simple Modal")
    def test_close_simple(self, driver):
        page = ModalsPage(driver)
        page.open()
        page.open_simple_modal()
        page.close_modal()
        assert not page.is_modal_visible()

    @allure.title("Позитив: открытие Form Modal")
    def test_open_form(self, driver):
        page = ModalsPage(driver)
        page.open()
        page.open_form_modal()
        assert page.is_modal_visible()

    @allure.title("Позитив: заполнение формы")
    def test_fill_form(self, driver):
        page = ModalsPage(driver)
        page.open()
        page.open_form_modal()
        page.fill_form("Ivan", "ivan@test.com")
        assert page.find(page.NAME_FIELD).get_attribute("value") == "Ivan"

    @allure.title("Негатив: пустая форма")
    def test_empty_form(self, driver):
        page = ModalsPage(driver)
        page.open()
        page.open_form_modal()
        page.submit()
        assert page.is_modal_visible()
