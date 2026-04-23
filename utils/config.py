import os

BASE_URL = os.getenv("BASE_URL", "https://demo.opencart.com")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
SLOW_MO = int(os.getenv("SLOW_MO", "0"))

# Test user credentials (demo site)
USER_EMAIL = os.getenv("USER_EMAIL", "test_playwright@example.com")
USER_PASSWORD = os.getenv("USER_PASSWORD", "Test@12345")
USER_FIRSTNAME = "Jaswanth"
USER_LASTNAME = "Tester"
USER_PHONE = "9999999999"

# Timeouts
DEFAULT_TIMEOUT = 15000  # 15s
