from pages.base_page import BasePage
from utils.config import BASE_URL


class WishlistPage(BasePage):
    URL = f"{BASE_URL}/index.php?route=account/wishlist"

    WISHLIST_ITEMS = ".table tbody tr"
    REMOVE_BUTTON = "button[data-original-title='Remove']"
    ADD_TO_CART_BUTTON = "button[data-original-title='Add to Cart']"
    EMPTY_TEXT = "p:has-text('Your wish list is empty')"
    SUCCESS_ALERT = ".alert-success"

    def load(self):
        self.navigate(self.URL)

    def is_empty(self) -> bool:
        return self.page.locator(self.EMPTY_TEXT).is_visible()

    def get_item_count(self) -> int:
        return len(self.page.locator(self.WISHLIST_ITEMS).all())

    def remove_item(self, index: int = 0):
        self.page.locator(self.REMOVE_BUTTON).nth(index).click()

    def move_to_cart(self, index: int = 0):
        self.page.locator(self.ADD_TO_CART_BUTTON).nth(index).click()
