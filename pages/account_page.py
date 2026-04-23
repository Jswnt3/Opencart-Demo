from pages.base_page import BasePage
from utils.config import BASE_URL


class AccountPage(BasePage):
    URL = f"{BASE_URL}/index.php?route=account/account"

    ACCOUNT_HEADING = "h2:has-text('My Account')"
    EDIT_ACCOUNT = "a:has-text('Edit Account')"
    CHANGE_PASSWORD = "a:has-text('Change Password')"
    ORDER_HISTORY = "a:has-text('Order History')"
    LOGOUT_LINK = "a:has-text('Logout')"
    WISHLIST_LINK = "a:has-text('Wish List')"

    # Edit form
    FIRSTNAME_INPUT = "#input-firstname"
    LASTNAME_INPUT = "#input-lastname"
    EMAIL_INPUT = "#input-email"
    PHONE_INPUT = "#input-telephone"
    SAVE_BUTTON = "input[value='Continue']"
    SUCCESS_ALERT = ".alert-success"

    def load(self):
        self.navigate(self.URL)

    def is_on_account_page(self) -> bool:
        return self.page.locator(self.ACCOUNT_HEADING).is_visible()

    def go_to_edit(self):
        self.click(self.EDIT_ACCOUNT)

    def update_name(self, firstname: str, lastname: str):
        self.go_to_edit()
        self.fill(self.FIRSTNAME_INPUT, firstname)
        self.fill(self.LASTNAME_INPUT, lastname)
        self.click(self.SAVE_BUTTON)

    def get_success_message(self) -> str:
        return self.get_text(self.SUCCESS_ALERT)

    def go_to_order_history(self):
        self.click(self.ORDER_HISTORY)

    def logout(self):
        self.click(self.LOGOUT_LINK)
