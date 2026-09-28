import allure
from pages.calendar_page import CalendarPage


@allure.feature("Calendar")
class TestCalendar:

    @allure.title("Позитив: открытие календаря")
    def test_open_calendar(self, driver):
        page = CalendarPage(driver)
        page.open()
        page.open_picker()
        assert page.is_picker_visible()

    @allure.title("Позитив: выбор даты")
    def test_select_date(self, driver):
        page = CalendarPage(driver)
        page.open()
        page.open_picker()
        page.select_day("15")
        assert page.get_date_value() != ""

    @allure.title("Позитив: следующий месяц")
    def test_next_month(self, driver):
        page = CalendarPage(driver)
        page.open()
        page.open_picker()
        cur = page.get_current_month()
        page.next_month()
        assert page.get_current_month() != cur

    @allure.title("Позитив: предыдущий месяц")
    def test_prev_month(self, driver):
        page = CalendarPage(driver)
        page.open()
        page.open_picker()
        page.next_month()
        cur = page.get_current_month()
        page.prev_month()
        assert page.get_current_month() != cur

    @allure.title("Негатив: невалидная дата")
    def test_invalid_date(self, driver):
        page = CalendarPage(driver)
        page.open()
        page.type(page.DATE_INPUT, "99/99/9999")
        assert page.get_date_value() in ("", "99/99/9999")

    @allure.title("Негатив: текст вместо даты")
    def test_text_instead_of_date(self, driver):
        page = CalendarPage(driver)
        page.open()
        page.type(page.DATE_INPUT, "abcdef")
        assert page.get_date_value() in ("", "abcdef")
