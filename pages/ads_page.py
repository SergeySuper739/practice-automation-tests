from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdsPage(BasePage):
    PATH = "/ads/"

    AD_BANNER = (By.CSS_SELECTOR, "ins.adsbygoogle, iframe[id^='aswift']")
    CLOSE_BTN = (By.CSS_SELECTOR, "[aria-label='Close'], .close-ad")

    def open(self):
        super().open(self.PATH)

    def is_ad_present(self):
        return len(self.driver.find_elements(*self.AD_BANNER)) > 0

    def close_ad_if_present(self):
        btns = self.driver.find_elements(*self.CLOSE_BTN)
        if btns:
            btns[0].click()
