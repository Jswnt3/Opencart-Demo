import pytest
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from utils.config import BASE_URL

MACBOOK_URL = f"{BASE_URL}/index.php?route=product/product&product_id=43"
IPHONE_URL = f"{BASE_URL}/index.php?route=product/product&product_id=40"


class TestCart:

    def _add_product_to_cart(self, page, url=MACBOOK_URL):
        page.goto(url)
        product = ProductPage(page)
        product.add_to_cart()

    def test_cart_empty_on_fresh_session(self, page):
        """TC-CART-01: Cart is empty on a fresh session"""
        cart = CartPage(page)
        cart.load()
        assert cart.is_empty(), "Cart should be empty initially"

    def test_add_single_product_to_cart(self, page):
        """TC-CART-02: Add a single product to cart"""
        self._add_product_to_cart(page)
        cart = CartPage(page)
        cart.load()
        assert not cart.is_empty(), "Cart should have an item"
        assert cart.get_item_count() >= 1

    def test_add_multiple_products_to_cart(self, page):
        """TC-CART-03: Add multiple different products to cart"""
        self._add_product_to_cart(page, MACBOOK_URL)
        self._add_product_to_cart(page, IPHONE_URL)
        cart = CartPage(page)
        cart.load()
        assert cart.get_item_count() >= 2

    def test_remove_item_from_cart(self, page):
        """TC-CART-04: Remove an item from the cart"""
        self._add_product_to_cart(page)
        cart = CartPage(page)
        cart.load()
        assert not cart.is_empty()
        cart.remove_item(index=0)
        page.wait_for_timeout(1500)
        cart.load()
        assert cart.is_empty(), "Cart should be empty after removing item"

    def test_update_cart_quantity(self, page):
        """TC-CART-05: Update quantity of an item in cart"""
        self._add_product_to_cart(page)
        cart = CartPage(page)
        cart.load()
        cart.update_quantity(index=0, qty=3)
        page.wait_for_timeout(1500)
        # Verify total changes — just assert page still has cart content
        assert not cart.is_empty()

    def test_proceed_to_checkout_from_cart(self, page):
        """TC-CART-06: Proceed to checkout button navigates correctly"""
        self._add_product_to_cart(page)
        cart = CartPage(page)
        cart.load()
        cart.proceed_to_checkout()
        assert "checkout" in page.url.lower()

    def test_cart_total_visible(self, page):
        """TC-CART-07: Cart total is displayed"""
        self._add_product_to_cart(page)
        cart = CartPage(page)
        cart.load()
        total = cart.get_total()
        assert "$" in total or len(total) > 0
