import pytest
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.home_page import HomePage
from utils.helpers import generate_email
from utils.config import USER_EMAIL, USER_PASSWORD, USER_FIRSTNAME, USER_LASTNAME, USER_PHONE


class TestAuthentication:

    def test_valid_login(self, page):
        """TC-AUTH-01: Valid login with correct credentials"""
        login = LoginPage(page)
        login.load()
        login.login(USER_EMAIL, USER_PASSWORD)
        assert login.is_logged_in(), "User should be logged in after valid credentials"

    def test_invalid_login_wrong_password(self, page):
        """TC-AUTH-02: Invalid login with wrong password"""
        login = LoginPage(page)
        login.load()
        login.login(USER_EMAIL, "WrongPassword123")
        error = login.get_error_message()
        assert "Warning" in error or "match" in error.lower(), f"Expected error, got: {error}"

    def test_invalid_login_empty_fields(self, page):
        """TC-AUTH-03: Login with empty fields"""
        login = LoginPage(page)
        login.load()
        login.login("", "")
        error = login.get_error_message()
        assert error is not None and len(error) > 0

    def test_login_with_invalid_email_format(self, page):
        """TC-AUTH-04: Login with invalid email format"""
        login = LoginPage(page)
        login.load()
        login.login("notanemail", "password123")
        error = login.get_error_message()
        assert error is not None

    def test_register_new_user(self, page):
        """TC-AUTH-05: Register a new account successfully"""
        register = RegisterPage(page)
        register.load()
        email = generate_email()
        register.register(USER_FIRSTNAME, USER_LASTNAME, email, USER_PHONE, USER_PASSWORD)
        assert register.is_registered(), "Registration should succeed with valid data"

    def test_register_existing_email(self, page):
        """TC-AUTH-06: Register with already existing email"""
        register = RegisterPage(page)
        register.load()
        register.register(USER_FIRSTNAME, USER_LASTNAME, USER_EMAIL, USER_PHONE, USER_PASSWORD)
        error = register.get_error()
        assert "Warning" in error or "already" in error.lower()

    def test_register_missing_required_fields(self, page):
        """TC-AUTH-07: Register without filling required fields"""
        register = RegisterPage(page)
        register.load()
        register.register("", "", "", "", "")
        # Should stay on register page with validation errors
        assert "register" in page.url.lower()

    def test_logout(self, page):
        """TC-AUTH-08: Logout after login"""
        login = LoginPage(page)
        login.load()
        login.login(USER_EMAIL, USER_PASSWORD)
        assert login.is_logged_in()
        home = HomePage(page)
        home.go_to_logout()
        assert "logout" in page.url.lower() or "account" in page.url.lower()

    def test_forgot_password_page_loads(self, page):
        """TC-AUTH-09: Forgot password link navigates correctly"""
        login = LoginPage(page)
        login.load()
        login.go_to_forgot_password()
        assert "forgotten" in page.url.lower()
