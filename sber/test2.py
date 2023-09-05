from pages.sbermarketing_page import SbermarketingPage
from pages.ya_page import YaPage


def test_second_scenario(browser):
    search_page = YaPage(browser)
    search_page.open()
    search_page.search_sbermarketing()
    sbermarketing_link = search_page.find_sbermarketing_link()
    search_page.click_on_element(sbermarketing_link)
    sbermarketing_page = SbermarketingPage(browser)
    sbermarketing_page.check_sbermarketing_page()



