import random
import string
from playwright.sync_api import Page


def generate_email():
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"playwright_{suffix}@testmail.com"


def generate_random_string(length=6):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def wait_and_click(page: Page, selector: str, timeout: int = 10000):
    page.wait_for_selector(selector, timeout=timeout)
    page.click(selector)


def wait_and_fill(page: Page, selector: str, value: str, timeout: int = 10000):
    page.wait_for_selector(selector, timeout=timeout)
    page.fill(selector, value)


def assert_success_alert(page: Page, expected_text: str = None):
    alert = page.locator(".alert-success")
    alert.wait_for(state="visible", timeout=10000)
    if expected_text:
        assert expected_text.lower() in alert.inner_text().lower()
    return alert.inner_text()


def assert_text_visible(page: Page, text: str):
    assert page.get_by_text(text, exact=False).is_visible(), f"Expected text '{text}' not visible"
