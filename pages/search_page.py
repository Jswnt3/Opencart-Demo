from pages.base_page import BasePage
from utils.config import BASE_URL


class SearchPage(BasePage):
    URL = f"{BASE_URL}/index.php?route=product/search"

    SEARCH_INPUT = "input[name='search']"
    SEARCH_BUTTON = "button.btn-default"
    PRODUCT_RESULTS = ".product-thumb"
    NO_RESULTS_TEXT = "p:has-text('There is no product')"
    RESULT_COUNT = "#content h1"

    def search(self, query: str):
        self.navigate(f"{self.URL}&search={query}")

    def get_results(self):
        return self.page.locator(self.PRODUCT_RESULTS).all()

    def get_result_count(self) -> int:
        return len(self.get_results())

    def has_no_results(self) -> bool:
        return self.page.locator(self.NO_RESULTS_TEXT).is_visible()

    def click_first_result(self):
        self.page.locator(self.PRODUCT_RESULTS).first.click()
