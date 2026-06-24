# Testing Rules

## Framework

* Framework: Playwright with Python + Pytest
* Browser automation: Playwright sync API unless async is specifically required.
* Test runner: Pytest

## Locator Strategy

* Prefer:

  * `page.get_by_role()`
  * `page.get_by_test_id()`
  * `page.get_by_label()`
  * `page.get_by_placeholder()`
* Avoid:

  * CSS class selectors (`.btn-primary`, `.login-form`, etc.)
  * Long XPath expressions.
* Use stable locators whenever possible.

### Good

```python
page.get_by_role("button", name="Login").click()
page.get_by_test_id("username").fill("admin")
```

### Bad

```python
page.locator(".login-btn").click()
page.locator("//div[2]/button").click()
```

---

## Folder Structure

```text
project/
│
├── tests/
│   ├── test_login.py
│   ├── test_dashboard.py
│   └── test_cart.py
│
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── cart_page.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── playwright.config.py (optional)
```

---

## Naming Conventions

### Test Files

```text
test_login.py
test_dashboard.py
test_checkout.py
```

### Page Objects

```text
login_page.py
dashboard_page.py
cart_page.py
```

### Classes

```python
class LoginPage:
class DashboardPage:
```

### Methods

```python
def login():
def add_to_cart():
```

---

## Assertions

Use multiple assertions carefully.

### Preferred

```python
assert page.get_by_text("Welcome").is_visible()
assert page.get_by_role("button", name="Logout").is_enabled()
```

For soft assertions:

```python
errors = []

if not page.get_by_text("Welcome").is_visible():
    errors.append("Welcome text not visible")

if not page.get_by_role("button", name="Logout").is_enabled():
    errors.append("Logout button not enabled")

assert not errors, "\n".join(errors)
```

---

## Wait Strategy

### Never use

```python
page.wait_for_timeout(5000)
time.sleep(5)
```

### Prefer

```python
page.get_by_role("button", name="Login").click()
page.wait_for_url("**/dashboard")
page.locator("#result").wait_for()
expect(page.get_by_text("Success")).to_be_visible()
```

---

## Page Object Model

### pages/login_page.py

```python
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.get_by_test_id("username")
        self.password = page.get_by_test_id("password")
        self.login_button = page.get_by_role("button", name="Login")

    def login(self, user, pwd):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_button.click()
```

---

## Test Example

```python
from pages.login_page import LoginPage

def test_valid_login(page):
    login = LoginPage(page)

    page.goto("https://example.com/login")
    login.login("admin", "admin123")

    assert page.get_by_text("Dashboard").is_visible()
```

---

## Run Commands

Run all tests:

```bash
pytest
```

Run with verbosity:

```bash
pytest -v
```

Run specific file:

```bash
pytest tests/test_login.py
```

Generate HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

Run in parallel:

```bash
pytest -n auto
```

---

## CI (GitHub Actions)

Use parallel execution with pytest-xdist.

```yaml
- name: Install dependencies
  run: |
    pip install -r requirements.txt
    playwright install

- name: Run tests
  run: pytest -n auto
```

---

## Additional Best Practices

* Keep tests independent.
* Use fixtures in `conftest.py`.
* Store test data separately.
* Use POM for maintainability.
* Capture screenshots on failure.
* Enable tracing for failed tests.
* Generate HTML reports after every execution.
