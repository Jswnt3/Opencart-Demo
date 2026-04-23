from pages.base_page import BasePage
from utils.config import BASE_URL


class CheckoutPage(BasePage):
    URL = f"{BASE_URL}/index.php?route=checkout/checkout"

    # Guest checkout
    GUEST_RADIO = "input[value='guest']"
    CONTINUE_GUEST_BTN = "#button-account"

    # Billing details
    BILLING_FIRSTNAME = "#input-payment-firstname"
    BILLING_LASTNAME = "#input-payment-lastname"
    BILLING_EMAIL = "#input-payment-email"
    BILLING_PHONE = "#input-payment-telephone"
    BILLING_ADDRESS = "#input-payment-address-1"
    BILLING_CITY = "#input-payment-city"
    BILLING_POSTCODE = "#input-payment-postcode"
    BILLING_COUNTRY = "#input-payment-country"
    BILLING_ZONE = "#input-payment-zone"
    CONTINUE_BILLING_BTN = "#button-payment-address"

    # Delivery
    CONTINUE_DELIVERY_BTN = "#button-shipping-address"
    CONTINUE_DELIVERY_METHOD_BTN = "#button-shipping-method"

    # Payment
    CONTINUE_PAYMENT_METHOD_BTN = "#button-payment-method"
    AGREE_TERMS = "input[name='agree']"
    CONFIRM_ORDER_BTN = "#button-confirm"

    SUCCESS_HEADING = "h1:has-text('Your order has been placed!')"
    ORDER_ID = "#content p strong"

    def load(self):
        self.navigate(self.URL)

    def checkout_as_guest(self, firstname, lastname, email, phone,
                          address, city, postcode, country="United Kingdom", zone=""):
        # Step 1 - Account
        self.page.locator(self.GUEST_RADIO).check()
        self.click(self.CONTINUE_GUEST_BTN)

        # Step 2 - Billing
        self.page.wait_for_selector(self.BILLING_FIRSTNAME, state="visible")
        self.fill(self.BILLING_FIRSTNAME, firstname)
        self.fill(self.BILLING_LASTNAME, lastname)
        self.fill(self.BILLING_EMAIL, email)
        self.fill(self.BILLING_PHONE, phone)
        self.fill(self.BILLING_ADDRESS, address)
        self.fill(self.BILLING_CITY, city)
        self.fill(self.BILLING_POSTCODE, postcode)
        self.page.select_option(self.BILLING_COUNTRY, label=country)
        self.page.wait_for_timeout(1000)
        if zone:
            self.page.select_option(self.BILLING_ZONE, label=zone)
        self.click(self.CONTINUE_BILLING_BTN)

        # Step 3 - Delivery
        self.page.wait_for_selector(self.CONTINUE_DELIVERY_BTN, state="visible")
        self.click(self.CONTINUE_DELIVERY_BTN)

        # Step 4 - Delivery method
        self.page.wait_for_selector(self.CONTINUE_DELIVERY_METHOD_BTN, state="visible")
        self.click(self.CONTINUE_DELIVERY_METHOD_BTN)

        # Step 5 - Payment method
        self.page.wait_for_selector(self.CONTINUE_PAYMENT_METHOD_BTN, state="visible")
        self.click(self.CONTINUE_PAYMENT_METHOD_BTN)

    def confirm_order(self):
        self.page.wait_for_selector(self.CONFIRM_ORDER_BTN, state="visible")
        self.click(self.CONFIRM_ORDER_BTN)

    def is_order_placed(self) -> bool:
        return self.page.locator(self.SUCCESS_HEADING).is_visible(timeout=15000)
