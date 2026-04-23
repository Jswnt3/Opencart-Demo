from pages.base_page import BasePage
from utils.config import BASE_URL


class RegisterPage(BasePage):
    URL = f"{BASE_URL}/index.php?route=account/register"

    FIRSTNAME = "#input-firstname"
    LASTNAME = "#input-lastname"
    EMAIL = "#input-email"
    TELEPHONE = "#input-telephone"
    PASSWORD = "#input-password"
    CONFIRM = "#input-confirm"
    AGREE_CHECKBOX = "input[name='agree']"
    SUBMIT_BUTTON = "input[value='Continue']"
    SUCCESS_HEADING = "h1:has-text('Your Account Has Been Created!')"
    ERROR_ALERT = ".alert-danger"

    def load(self):
        self.navigate(self.URL)

    def register(self, firstname, lastname, email, phone, password):
        self.fill(self.FIRSTNAME, firstname)
        self.fill(self.LASTNAME, lastname)
        self.fill(self.EMAIL, email)
        self.fill(self.TELEPHONE, phone)
        self.fill(self.PASSWORD, password)
        self.fill(self.CONFIRM, password)
        self.page.locator(self.AGREE_CHECKBOX).check()
        self.click(self.SUBMIT_BUTTON)

    def is_registered(self) -> bool:
        return self.page.locator(self.SUCCESS_HEADING).is_visible()

    def get_error(self) -> str:
        return self.get_text(self.ERROR_ALERT)
