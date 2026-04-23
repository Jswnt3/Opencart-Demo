from pages.base_page import BasePage
from utils.config import BASE_URL


class LoginPage(BasePage):
    URL = f"{BASE_URL}/index.php?route=account/login"

    EMAIL_INPUT = "#input-email"
    PASSWORD_INPUT = "#input-password"
    LOGIN_BUTTON = "input[value='Login']"
    FORGOT_PASSWORD = "a:has-text('Forgotten Password')"
    ERROR_ALERT = ".alert-danger"
    ACCOUNT_HEADING = "h2:has-text('My Account')"

    def load(self):
        self.navigate(self.URL)

    def login(self, email: str, password: str):
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_ALERT)

    def is_logged_in(self) -> bool:
        return self.page.locator(self.ACCOUNT_HEADING).is_visible()

    def go_to_forgot_password(self):
        self.click(self.FORGOT_PASSWORD)
