from pages.base_page import BasePage


class MRMPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._base_url = "https://mrm.sbermarketing.ru/"

    def check_page(self):
        assert self.driver.current_url.startswith("https://auth.sbermarketing.ru/interaction/")
