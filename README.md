# 🎭 Opencart-Demo — Playwright E2E Automation Framework

> Production-grade test automation framework built with Playwright + Python covering 15+ critical user workflows on OpenCart demo site.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

---

## 📊 Coverage at a Glance

| 🧪 Test Cases | 🔄 Workflows | 🌐 Browsers | 🎯 Code Coverage | ⚡ CI/CD |
|:---:|:---:|:---:|:---:|:---:|
| **60+** | **15+** | **Chrome & Firefox** | **90%+** | **GitHub Actions** |

---

## 🗂️ Project Structure

```
opencart-playwright/
├── .github/workflows/       # GitHub Actions CI/CD pipeline
├── pages/                   # Page Object Models
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── register_page.py
│   ├── search_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── wishlist_page.py
│   └── account_page.py
├── tests/                   # Test suites
│   ├── test_auth.py         # 9 test cases — login, register, logout
│   ├── test_search.py       # 6 test cases — search workflows
│   ├── test_product.py      # 7 test cases — product interactions
│   ├── test_cart.py         # 7 test cases — cart management
│   └── test_wishlist.py     # 3 test cases — wishlist workflows
├── utils/
│   ├── config.py            # Central config — BASE_URL, credentials
│   └── helpers.py           # Reusable utility functions
├── conftest.py              # Shared fixtures + tracing setup
├── pytest.ini               # Pytest configuration
└── requirements.txt         # Dependencies
```

---

## ✅ What's Tested

| Module | Workflows Covered |
|---|---|
| 🔐 Auth | Login, Register, Logout, Forgot Password |
| 🔍 Search | Valid search, No results, Empty query, Case insensitive |
| 📦 Product | Add to cart, Wishlist, Reviews, Breadcrumb |
| 🛒 Cart | Add, Remove, Update qty, Checkout flow |
| ❤️ Wishlist | Add, Remove, Move to cart |

---

## 🚀 How to Run

**1. Install dependencies**
```bash
pip install -r requirements.txt
playwright install chromium firefox
```

**2. Run all tests**
```bash
pytest
```

**3. Run specific module**
```bash
pytest tests/test_auth.py
pytest tests/test_cart.py
```

**4. Run headed (see the browser)**
```bash
HEADLESS=false pytest tests/test_search.py
```

**5. Run in parallel**
```bash
pytest -n 4
```

**6. View HTML report**
```bash
open reports/report.html
```

---

## ⚙️ CI/CD

Every push and pull request to `main`/`master` automatically:
- Installs dependencies
- Runs full test suite on Ubuntu (headless)
- Uploads HTML report as a downloadable artifact

---

## 🏗️ Key Design Decisions

- **Page Object Model** — every page is a separate class, keeping tests clean and maintainable
- **Playwright Tracing** — traces saved on failure for easy debugging
- **Resilient Locators** — no fragile XPaths; uses semantic selectors to eliminate flaky failures
- **Central Config** — all URLs, credentials, and timeouts in one place via `utils/config.py`

---

## 👤 Author

**Jaswanth Mudapaka**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/jaswanth-mudapaka)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Jswnt3)
[![Portfolio](https://img.shields.io/badge/Portfolio-FF9500?style=flat-square&logo=firefoxbrowser&logoColor=white)](https://jswnt3.github.io)
