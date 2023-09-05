import pytest

from pages.google_page import GooglePage
from pages.ya_page import YaPage

SEARCHER_ENGINES = {
    "ya": YaPage,
    "google": GooglePage,
 }


@pytest.mark.parametrize("searcher_engine", ["ya", "google"])
def test_first_scenario(browser, searcher_engine):
    search_page = SEARCHER_ENGINES[searcher_engine](browser)
    search_page.open()
    search_page.search_sbermarketing()
    search_page.check_sbermarketing_link()
