# Playwright + Pytest Framework for SauceDemo

Build a production-grade, Page Object Model (POM) test automation framework targeting [saucedemo.com](https://www.saucedemo.com). The `rules.md` file was empty, so the framework follows industry-standard Playwright + Pytest conventions.

---

## Proposed Structure

```
e:\antigravity-projects\GoDigit_ML\
├── conftest.py                          # Root fixtures: browser, context, page, login helper
├── pytest.ini                           # Pytest config: markers, reports, base URL
├── requirements.txt                     # Python dependencies
├── pages/
│   ├── __init__.py
│   ├── base_page.py                     # BasePage with shared helpers (wait, screenshot, etc.)
│   ├── login_page.py                    # LoginPage POM
│   ├── inventory_page.py                # InventoryPage POM
│   ├── cart_page.py                     # CartPage POM
│   └── checkout_page.py                 # CheckoutPage POM (info + overview + complete)
├── tests/
│   ├── __init__.py
│   ├── test_login.py                    # Login test cases
│   ├── test_add_to_cart.py              # Add-to-cart test cases
│   └── test_checkout.py                 # Checkout flow test cases
├── utils/
│   ├── __init__.py
│   └── test_data.py                     # Centralized test data / credentials
├── reports/                             # HTML reports (auto-generated)
└── screenshots/                         # Failure screenshots (auto-generated)
```

---

## Proposed Changes

### Configuration

#### [NEW] pytest.ini
- Base URL, markers (`smoke`, `regression`, `checkout`), HTML report output, asyncio mode, retries.

#### [NEW] requirements.txt
- `pytest`, `pytest-playwright`, `pytest-html`, `pytest-rerunfailures`, `Faker`

---

### Pages

#### [NEW] pages/base_page.py
- `BasePage` class wrapping `playwright.Page`
- Shared: `navigate()`, `take_screenshot()`, `wait_for_element()`, `get_text()`

#### [NEW] pages/login_page.py
- `LoginPage(BasePage)`: `login(username, password)`, `get_error_message()`, `is_logged_in()`

#### [NEW] pages/inventory_page.py
- `InventoryPage(BasePage)`: `add_item_to_cart(name)`, `get_cart_count()`, `open_cart()`, `get_all_product_names()`, `sort_products(option)`

#### [NEW] pages/cart_page.py
- `CartPage(BasePage)`: `get_cart_items()`, `remove_item(name)`, `proceed_to_checkout()`

#### [NEW] pages/checkout_page.py
- `CheckoutPage(BasePage)`: `fill_info(first, last, zip)`, `continue_checkout()`, `finish_checkout()`, `get_order_confirmation()`, `get_item_total()`

---

### Fixtures (`conftest.py`)

- **`browser_context`** — new Playwright browser context with tracing enabled
- **`page`** — fresh page per test
- **`logged_in_page`** — page already authenticated as `standard_user`
- **`take_screenshot`** — callable fixture that saves to `screenshots/`
- Auto-capture screenshot + stop trace on **test failure**
- HTML report auto-generated via `pytest-html`

---

### Tests

#### [NEW] tests/test_login.py
| Test | Marker |
|------|--------|
| Valid login (standard_user) | smoke |
| Locked-out user shows error | smoke |
| Invalid credentials error | regression |
| Empty username/password | regression |
| Problem user login | regression |

#### [NEW] tests/test_add_to_cart.py
| Test | Marker |
|------|--------|
| Add single item to cart | smoke |
| Add multiple items to cart | smoke |
| Remove item from cart | regression |
| Cart badge count reflects adds | regression |
| Sort products by price (low→high) | regression |

#### [NEW] tests/test_checkout.py
| Test | Marker |
|------|--------|
| Full checkout flow (happy path) | smoke |
| Checkout with empty cart | regression |
| Missing first name validation | regression |
| Missing last name validation | regression |
| Missing zip code validation | regression |
| Cancel from checkout info | regression |
| Cancel from checkout overview | regression |

---

## Verification Plan

### Automated
```bash
pip install -r requirements.txt
playwright install chromium
pytest tests/ --html=reports/report.html --self-contained-html -v
```

### Manual Verification
- HTML report opens correctly in `reports/report.html`
- Traces viewable at `playwright show-trace <trace.zip>`
- Screenshots appear in `screenshots/` on failures
