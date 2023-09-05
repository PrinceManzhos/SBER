from pages.mrm_page import MRMPage
from pages.sbermarketing_page import SbermarketingPage


def test_third_scenario(browser):
    sbermarketing_page = SbermarketingPage(browser)
    sbermarketing_page.open()
    sbermarketing_page.close_cookies()
    sbermarketing_page.go_to_mrm()
    mrm_page = MRMPage(browser)
    mrm_page.check_page()