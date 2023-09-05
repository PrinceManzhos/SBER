from pages.base_page import BasePage
from pages.locators import SbermarketPageLocators


class SbermarketingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._base_url = "https://sbermarketing.ru/"

    def check_sbermarketing_page(self):
        assert self.get_current_url() == self._base_url, "Осуществлен переход на некорректный сайт"

    def close_cookies(self):
        self.click_on_element(SbermarketPageLocators.CLOSE_COOKIES)

    def go_to_mrm(self):
        self.click_on_element(SbermarketPageLocators.ENTRY_MRM)
        self.switch_window()






