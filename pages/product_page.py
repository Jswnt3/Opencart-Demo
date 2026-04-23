from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_TITLE = "h1"
    ADD_TO_CART_BUTTON = "button[id='button-cart']"
    ADD_TO_WISHLIST = "button[data-original-title='Add to Wish List']"
    ADD_TO_COMPARE = "button[data-original-title='Compare this Product']"
    QUANTITY_INPUT = "#input-quantity"
    SUCCESS_ALERT = ".alert-success"
    PRICE = ".price-new, h2.price"
    PRODUCT_DESCRIPTION = "#tab-description"
    REVIEW_TAB = "a[href='#tab-review']"
    REVIEW_NAME = "#input-name"
    REVIEW_TEXT = "#input-review"
    REVIEW_RATING = "input[name='rating']"
    REVIEW_SUBMIT = "#button-review"
    BREADCRUMB = ".breadcrumb"

    def get_product_name(self) -> str:
        return self.get_text(self.PRODUCT_TITLE)

    def add_to_cart(self, quantity: int = 1):
        self.fill(self.QUANTITY_INPUT, str(quantity))
        self.click(self.ADD_TO_CART_BUTTON)
        self.page.locator(self.SUCCESS_ALERT).wait_for(state="visible", timeout=10000)

    def add_to_wishlist(self):
        self.click(self.ADD_TO_WISHLIST)

    def add_to_compare(self):
        self.click(self.ADD_TO_COMPARE)

    def get_price(self) -> str:
        return self.get_text(self.PRICE)

    def open_review_tab(self):
        self.click(self.REVIEW_TAB)

    def submit_review(self, name: str, review: str, rating: int = 5):
        self.open_review_tab()
        self.fill(self.REVIEW_NAME, name)
        self.fill(self.REVIEW_TEXT, review)
        self.page.locator(f"input[name='rating'][value='{rating}']").check()
        self.click(self.REVIEW_SUBMIT)

    def get_success_message(self) -> str:
        return self.get_text(self.SUCCESS_ALERT)
