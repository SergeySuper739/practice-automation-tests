from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FormPage(BasePage):
    PATH = "/popups/"

    MESSAGE_FIELD = (By.ID, "message")
    AUTOMATION_TOOLS = (By.XPATH, "//h3[contains(text(),'Automation Tools')]/following-sibling::ul/li")

    def open(self):
        super().open(self.PATH)

    def get_automation_tools(self):
        elements = self.driver.find_elements(*self.AUTOMATION_TOOLS)
        return [el.text.strip() for el in elements if el.text.strip()]

    def fill_message_from_tools(self):
        tools = self.get_automation_tools()
        text = ", ".join(tools)
        self.type(self.MESSAGE_FIELD, text)
        return text

    def get_message_value(self):
        return self.find(self.MESSAGE_FIELD).get_attribute("value")
