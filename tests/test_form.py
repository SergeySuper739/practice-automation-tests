import allure
from pages.form_page import FormPage


@allure.feature("Form / Automation Tools")
class TestForm:

    @allure.title("Заполнение Message списком Automation Tools")
    def test_fill_message_with_tools(self, driver):
        page = FormPage(driver)
        page.open()
        filled = page.fill_message_from_tools()
        assert page.get_message_value() == filled
        assert "," in filled

    @allure.title("Негатив: пустое Message")
    def test_empty_message(self, driver):
        page = FormPage(driver)
        page.open()
        assert page.get_message_value() == ""
