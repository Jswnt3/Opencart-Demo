import pytest
from pages.search_page import SearchPage
from pages.home_page import HomePage


class TestSearch:

    def test_search_valid_product(self, page):
        """TC-SRCH-01: Search for an existing product"""
        search = SearchPage(page)
        search.search("MacBook")
        assert search.get_result_count() > 0, "Search should return results for 'MacBook'"

    def test_search_no_results(self, page):
        """TC-SRCH-02: Search for a non-existent product"""
        search = SearchPage(page)
        search.search("xyzproductnotexist12345")
        assert search.has_no_results(), "Should show no results message for invalid query"

    def test_search_from_homepage(self, page):
        """TC-SRCH-03: Search using the homepage search bar"""
        home = HomePage(page)
        home.search("iPhone")
        assert "search" in page.url.lower()

    def test_search_empty_query(self, page):
        """TC-SRCH-04: Search with empty query"""
        home = HomePage(page)
        home.search("")
        # Should navigate to search page and handle gracefully
        assert "search" in page.url.lower()

    def test_search_result_click(self, page):
        """TC-SRCH-05: Click on a search result navigates to product"""
        search = SearchPage(page)
        search.search("MacBook")
        search.click_first_result()
        assert "product" in page.url.lower()

    def test_search_case_insensitive(self, page):
        """TC-SRCH-06: Search is case insensitive"""
        search = SearchPage(page)
        search.search("macbook")
        lower_count = search.get_result_count()
        search.search("MACBOOK")
        upper_count = search.get_result_count()
        assert lower_count == upper_count, "Search should be case insensitive"
