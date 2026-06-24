# SauceDemo Playwright + Pytest Framework — Walkthrough

## ✅ Final Test Results

```
32 passed, 3 rerun in 865.93s (0:14:25)
```

> **32/32 tests passed. Zero failures.**  
> 3 tests hit timing issues on first attempt and auto-retried via `pytest-rerunfailures` — all passed on rerun.

---

## Test Breakdown

| Suite | Tests | Result | Reruns |
|---|---|---|---|
| `test_add_to_cart.py` | 11 | ✅ All passed | 0 |
| `test_checkout.py` | 10 | ✅ All passed | 2 |
| `test_login.py` | 7 | ✅ All passed | 1 |
| **Total** | **32** | **✅ 32 passed** | **3** |

---

## What Was Built

### Project Structure
```
e:\antigravity-projects\GoDigit_ML\
├── conftest.py                  # Root fixtures + pytest hooks
├── pytest.ini                   # Config: markers, HTML report, reruns
├── requirements.txt             # Dependencies
├── pages/
│   ├── base_page.py             # BasePage: shared helpers
│   ├── login_page.py            # LoginPage POM
│   ├── inventory_page.py        # InventoryPage POM
│   ├── cart_page.py             # CartPage POM
│   └── checkout_page.py        # CheckoutPage POM (3 steps)
├── utils/
│   └── test_data.py             # Credentials, products, error messages
├── tests/
│   ├── test_login.py            # 7 login tests
│   ├── test_add_to_cart.py      # 11 cart/inventory tests
│   └── test_checkout.py        # 10 checkout flow tests
├── reports/
│   └── report.html              # ✅ Auto-generated HTML report
├── screenshots/                 # Auto-captured on failure
└── traces/                      # Auto-captured trace.zip on failure
```

### Key Framework Features
- **Page Object Model** — `BasePage` + 4 specialized POMs, all selector-centralized
- **Auto-login fixture** — `logged_in_page` authenticates before every test that needs it
- **Failure artifacts** — full-page screenshot + Playwright trace captured automatically on any test failure
- **HTML report** — generated at `reports/report.html` after every run
- **Auto-retry** — `pytest-rerunfailures` retries flaky tests once with a 2s delay
- **Markers** — `smoke`, `regression`, `checkout`, `login`, `cart` for selective runs

---

## Artifacts

| Artifact | Path |
|---|---|
| HTML Report | [report.html](file:///E:/antigravity-projects/GoDigit_ML/reports/report.html) |
| Failure Screenshots | [screenshots/](file:///E:/antigravity-projects/GoDigit_ML/screenshots) |
| Playwright Traces | [traces/](file:///E:/antigravity-projects/GoDigit_ML/traces) |

---

## Useful Run Commands

```bash
# Run all tests with HTML report
pytest tests/ --html=reports/report.html --self-contained-html -v

# Run only smoke tests
pytest tests/ -m smoke -v

# Run only login tests
pytest tests/ -m login -v

# Run headed (see browser)
pytest tests/ --headed -v

# Run a specific file
pytest tests/test_checkout.py -v

# View a Playwright trace
playwright show-trace traces/<trace-file>.zip
```
