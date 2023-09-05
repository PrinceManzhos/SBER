from pages.locators import GooglePageLocators
from pages.search_base_page import SearchBasePage


class GooglePage(SearchBasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = GooglePageLocators
        self._base_url = "https://google.com/"

    # def search_sbermarketing(self):
    #     self.send_keys(GooglePageLocators.FIND_INPUT, "sbermarketing")
    #     self.click_on_element(GooglePageLocators.FIND_BUTTON)
    #
    # def check_sbermarketing_link(self):
    #     result = self.find_elements(GooglePageLocators.FOUND_LINKS)
    #     assert any(elem.get_attribute("href") == "https://sbermarketing.ru/" for elem in result), "Ссылка некорректна"
