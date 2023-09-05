from pages.locators import YaPageLocators
from pages.search_base_page import SearchBasePage


class YaPage(SearchBasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = YaPageLocators
        self._base_url = "https://ya.ru/"
