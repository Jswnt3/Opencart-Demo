import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.wishlist_page import WishlistPage
from utils.config import BASE_URL, USER_EMAIL, USER_PASSWORD

MACBOOK_URL = f"{BASE_URL}/index.php?route=product/product&product_id=43"


def login_user(page):
    login = LoginPage(page)
    login.load()
    login.login(USER_EMAIL, USER_PASSWORD)


class TestWishlist:

    def test_add_to_wishlist_when_logged_in(self, page):
        """TC-WISH-01: Add product to wishlist when logged in"""
        login_user(page)
        page.goto(MACBOOK_URL)
        product = ProductPage(page)
        product.add_to_wishlist()
        page.wait_for_timeout(1000)
        alert_text = page.locator(".alert").inner_text()
        assert "wish list" in alert_text.lower()

    def test_wishlist_page_accessible(self, page):
        """TC-WISH-02: Wishlist page loads after login"""
        login_user(page)
        wishlist = WishlistPage(page)
        wishlist.load()
        assert "wishlist" in page.url.lower() or "wish_list" in page.url.lower()

    def test_add_to_wishlist_redirects_if_not_logged_in(self, page):
        """TC-WISH-03: Wishlist requires login"""
        page.goto(MACBOOK_URL)
        product = ProductPage(page)
        product.add_to_wishlist()
        page.wait_for_timeout(1000)
        # Should either show login prompt or redirect
        assert "login" in page.url.lower() or page.locator(".alert").is_visible()
