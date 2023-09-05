from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self._base_url = None

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Не нашлось элемента по локатору {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Не нашлось элемента по локатору {locator}")

    def click_on_element(self, locator, time=10):
        web_element = self.find_element(locator) if isinstance(locator, tuple) else locator
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(web_element),
                                               message=f"Элемент по локатору {web_element} не кликабелен").click()

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def open(self, url=None):
        if not url:
            if self._base_url:
                self.driver.get(self._base_url)
        elif url:
            self.driver.get(url)
        else:
            raise Exception('URL не установлен')

    def go_to_site(self):
        if self._base_url is None:
            raise AttributeError(f"Переход на {type(self)} невозможен")
        self.driver.get(self._base_url)

    def get_current_url(self):
        return self.driver.current_url

    def switch_window(self, n=-1):
        self.driver.switch_to.window(self.driver.window_handles[n])