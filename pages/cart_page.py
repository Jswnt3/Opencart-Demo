from pages.base_page import BasePage
from utils.config import BASE_URL


class CartPage(BasePage):
    URL = f"{BASE_URL}/index.php?route=checkout/cart"

    CART_TABLE = ".table-responsive"
    CART_ITEMS = ".table tbody tr"
    QUANTITY_INPUT = "input.form-control[type='text']"
    UPDATE_BUTTON = "button[data-original-title='Update']"
    REMOVE_BUTTON = "button[data-original-title='Remove']"
    CHECKOUT_BUTTON = "a:has-text('Checkout')"
    EMPTY_CART_TEXT = "p:has-text('Your shopping cart is empty')"
    COUPON_INPUT = "#input-coupon"
    COUPON_APPLY = "#button-coupon"
    SUCCESS_ALERT = ".alert-success"
    DANGER_ALERT = ".alert-danger"
    SUBTOTAL = "tr:has-text('Sub-Total') td:last-child"
    TOTAL = "tr:has-text('Total') td:last-child"

    def load(self):
        self.navigate(self.URL)

    def is_empty(self) -> bool:
        return self.page.locator(self.EMPTY_CART_TEXT).is_visible()

    def get_item_count(self) -> int:
        return len(self.page.locator(self.CART_ITEMS).all())

    def update_quantity(self, index: int, qty: int):
        inputs = self.page.locator(self.QUANTITY_INPUT).all()
        inputs[index].fill(str(qty))
        self.page.locator(self.UPDATE_BUTTON).nth(index).click()

    def remove_item(self, index: int = 0):
        self.page.locator(self.REMOVE_BUTTON).nth(index).click()

    def apply_coupon(self, code: str):
        self.fill(self.COUPON_INPUT, code)
        self.click(self.COUPON_APPLY)

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def get_total(self) -> str:
        return self.get_text(self.TOTAL)
