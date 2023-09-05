from selenium.webdriver.common.by import By


class YaPageLocators:
    FIND_INPUT = (By.ID, "text")
    FIND_BUTTON = (By.CSS_SELECTOR, "button.search3__button")
    FOUND_LINKS = (By.CSS_SELECTOR, ".organic__subtitle > div > a")


class GooglePageLocators:
    FIND_INPUT = (By.ID, "APjFqb")
    FIND_BUTTON = (By.CSS_SELECTOR, ".UUbT9 input.gNO89b")
    FOUND_LINKS = (By.CSS_SELECTOR, "#rso .yuRUbf a")


class SbermarketPageLocators:
    CLOSE_COOKIES = (By.CSS_SELECTOR, "#cookie span")
    ENTRY_MRM = (By.CSS_SELECTOR, "a.header__mrm")
