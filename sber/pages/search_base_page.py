import time

from pages.base_page import BasePage


class SearchBasePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = None

    def search_sbermarketing(self):
        if self.locators is None:
            raise AttributeError
        self.send_keys(self.locators.FIND_INPUT, "sbermarketing")
        self.click_on_element(self.locators.FIND_BUTTON)

    def find_sbermarketing_link(self):
        links = self.find_elements(self.locators.FOUND_LINKS)
        sbermarketing_url = "https://sbermarketing.ru/"
        for a in links:
            if a.get_attribute("href") == sbermarketing_url:
                return a

    def check_sbermarketing_link(self):
        assert self.find_sbermarketing_link(), "Ссылка некорректна"




