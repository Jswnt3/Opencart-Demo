from playwright.sync_api import Page
from utils.config import DEFAULT_TIMEOUT


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.page.set_default_timeout(DEFAULT_TIMEOUT)

    def navigate(self, url: str):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()

    def click(self, selector: str):
        self.page.locator(selector).click()

    def fill(self, selector: str, value: str):
        self.page.locator(selector).fill(value)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()
