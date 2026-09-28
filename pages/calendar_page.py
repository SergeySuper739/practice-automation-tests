from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CalendarPage(BasePage):
    PATH = "/calendars/"

    DATE_INPUT = (By.ID, "g1065-2-1-2-select-date")
    PICKER = (By.CLASS_NAME, "ui-datepicker")
    NEXT_MONTH = (By.CSS_SELECTOR, ".ui-datepicker-next")
    PREV_MONTH = (By.CSS_SELECTOR, ".ui-datepicker-prev")
    CURRENT_MONTH = (By.CLASS_NAME, "ui-datepicker-month")

    def open(self):
        super().open(self.PATH)

    def open_picker(self):
        self.click(self.DATE_INPUT)

    def is_picker_visible(self):
        return self.is_visible(self.PICKER)

    def select_day(self, day="15"):
        self.driver.find_element(By.XPATH, f"//a[text()='{day}']").click()

    def next_month(self):
        self.click(self.NEXT_MONTH)

    def prev_month(self):
        self.click(self.PREV_MONTH)

    def get_current_month(self):
        return self.find(self.CURRENT_MONTH).text

    def get_date_value(self):
        return self.find(self.DATE_INPUT).get_attribute("value")
