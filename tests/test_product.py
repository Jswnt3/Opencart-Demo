import pytest
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from utils.config import BASE_URL


MACBOOK_URL = f"{BASE_URL}/index.php?route=product/product&product_id=43"


class TestProduct:

    def test_product_page_loads(self, page):
        """TC-PROD-01: Product detail page loads correctly"""
        page.goto(MACBOOK_URL)
        product = ProductPage(page)
        name = product.get_product_name()
        assert len(name) > 0, "Product name should be visible"

    def test_product_price_visible(self, page):
        """TC-PROD-02: Product price is displayed"""
        page.goto(MACBOOK_URL)
        product = ProductPage(page)
        price = product.get_price()
        assert "$" in price or "£" in price or len(price) > 0

    def test_add_to_cart(self, page):
        """TC-PROD-03: Add product to cart"""
        page.goto(MACBOOK_URL)
        product = ProductPage(page)
        product.add_to_cart(quantity=1)
        msg = product.get_success_message()
        assert "cart" in msg.lower() or "success" in msg.lower()

    def test_add_to_cart_multiple_qty(self, page):
        """TC-PROD-04: Add multiple quantity to cart"""
        page.goto(MACBOOK_URL)
        product = ProductPage(page)
        product.add_to_cart(quantity=2)
        msg = product.get_success_message()
        assert "cart" in msg.lower()

    def test_add_to_wishlist_requires_login(self, page):
        """TC-PROD-05: Adding to wishlist redirects to login if not logged in"""
        page.goto(MACBOOK_URL)
        product = ProductPage(page)
        product.add_to_wishlist()
        # Should show login alert or redirect
        assert "login" in page.url.lower() or page.locator(".alert").is_visible()

    def test_product_breadcrumb(self, page):
        """TC-PROD-06: Breadcrumb navigation is visible"""
        page.goto(MACBOOK_URL)
        product = ProductPage(page)
        assert product.is_visible(product.BREADCRUMB), "Breadcrumb should be visible"

    def test_product_review_tab(self, page):
        """TC-PROD-07: Review tab opens correctly"""
        page.goto(MACBOOK_URL)
        product = ProductPage(page)
        product.open_review_tab()
        assert product.is_visible(product.REVIEW_NAME), "Review form should be visible"
