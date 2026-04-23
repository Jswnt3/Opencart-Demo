from pages.base_page import BasePage


class HomePage(BasePage):
    # Locators
    SEARCH_INPUT = "input[name='search']"
    SEARCH_BUTTON = "button.btn-default[type='button']"
    NAV_MY_ACCOUNT = "a:has-text('My Account')"
    NAV_LOGIN = "a:has-text('Login')"
    NAV_REGISTER = "a:has-text('Register')"
    NAV_LOGOUT = "a:has-text('Logout')"
    CART_BUTTON = "#cart > button"
    FEATURED_PRODUCTS = ".product-thumb"
    CURRENCY_DROPDOWN = ".btn-group .dropdown-toggle"

    def search(self, query: str):
        self.fill(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)

    def go_to_login(self):
        self.page.hover(self.NAV_MY_ACCOUNT)
        self.page.locator(self.NAV_LOGIN).click()

    def go_to_register(self):
        self.page.hover(self.NAV_MY_ACCOUNT)
        self.page.locator(self.NAV_REGISTER).click()

    def go_to_logout(self):
        self.page.hover(self.NAV_MY_ACCOUNT)
        self.page.locator(self.NAV_LOGOUT).click()

    def open_cart(self):
        self.click(self.CART_BUTTON)

    def get_featured_products(self):
        return self.page.locator(self.FEATURED_PRODUCTS).all()

    def change_currency(self, currency: str):
        self.click(self.CURRENCY_DROPDOWN)
        self.page.locator(f"button[name='{currency}']").click()
