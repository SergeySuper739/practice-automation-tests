from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ModalsPage(BasePage):
    PATH = "/modals/"

    SIMPLE_MODAL_BTN = (By.XPATH, "//button[text()='Simple Modal']")
    FORM_MODAL_BTN = (By.XPATH, "//button[text()='Form Modal']")
    MODAL = (By.CLASS_NAME, "modal")
    CLOSE_BTN = (By.CSS_SELECTOR, ".modal .close")
    NAME_FIELD = (By.ID, "name")
    EMAIL_FIELD = (By.ID, "email")
    SUBMIT_BTN = (By.XPATH, "//button[text()='Submit']")

    def open(self):
        super().open(self.PATH)

    def open_simple_modal(self):
        self.click(self.SIMPLE_MODAL_BTN)

    def open_form_modal(self):
        self.click(self.FORM_MODAL_BTN)

    def is_modal_visible(self):
        return self.is_visible(self.MODAL)

    def close_modal(self):
        self.click(self.CLOSE_BTN)

    def fill_form(self, name, email):
        self.type(self.NAME_FIELD, name)
        self.type(self.EMAIL_FIELD, email)

    def submit(self):
        self.click(self.SUBMIT_BTN)
