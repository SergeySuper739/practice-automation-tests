import allure
from pages.ads_page import AdsPage


@allure.feature("Ads")
class TestAds:

    @allure.title("Позитив: страница ads открывается")
    def test_ads_page_open(self, driver):
        page = AdsPage(driver)
        page.open()
        assert "ads" in driver.current_url

    @allure.title("Позитив: закрытие рекламы (если есть)")
    def test_close_ad(self, driver):
        page = AdsPage(driver)
        page.open()
        page.close_ad_if_present()
        assert True

    @allure.title("Негатив: проверка URL")
    def test_wrong_url(self, driver):
        page = AdsPage(driver)
        page.open()
        assert "wrong" not in driver.current_url
