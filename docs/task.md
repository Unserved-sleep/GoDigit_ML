# SauceDemo Playwright Framework - Tasks

## Configuration
- [x] `pytest.ini`
- [x] `requirements.txt`

## Pages
- [x] `pages/__init__.py`
- [x] `pages/base_page.py`
- [x] `pages/login_page.py`
- [x] `pages/inventory_page.py`
- [x] `pages/cart_page.py`
- [x] `pages/checkout_page.py`

## Utils
- [x] `utils/__init__.py`
- [x] `utils/test_data.py`

## Fixtures
- [x] `conftest.py`

## Tests
- [x] `tests/__init__.py`
- [x] `tests/test_login.py`
- [x] `tests/test_add_to_cart.py`
- [x] `tests/test_checkout.py`

## Verification
- [ ] Run `pip install -r requirements.txt`
- [ ] Run `playwright install chromium`
- [ ] Run `pytest tests/ --html=reports/report.html -v`
