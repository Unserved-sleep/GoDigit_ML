# Testing Rules

* Framework: Playwright with Python and Pytest
* Browser automation: Playwright sync API
* Locator strategy: prefer get_by_role, get_by_test_id. Never use CSS class selectors.
* Folder structure:

  * tests/ for test files
  * pages/ for page objects
  * utils/ for helpers
  * reports/ for HTML reports
  * screenshots/ for screenshots
  * traces/ for Playwright traces
* Naming:

  * test files: test_login.py, test_cart_flow.py
  * page objects: login_page.py, cart_page.py
  * classes: LoginPage, CartPage
* Assertions: use pytest assertions. When multiple validations exist, collect failures and report all of them.
* Avoid all hard waits:

  * never use time.sleep()
  * never use page.wait_for_timeout()
  * rely on Playwright auto-waiting and explicit conditions.
* Use Page Object Model.
* Use pytest fixtures in conftest.py.
* Create reusable browser, context, and page fixtures.
* Capture screenshots on test failures.
* Save Playwright traces on failures.
* Generate pytest-html reports.
* Store test data in separate files when appropriate.
* Tests should be independent and runnable individually.
* Prefer environment variables over hardcoded credentials.
* Generate production-quality code with comments.
* When creating new tests, automatically create the required page objects and fixtures if they do not exist.
* When generating a framework, automatically create all folders and files required by the framework.
* Run command: pytest
* HTML report command:
  pytest --html=reports/report.html --self-contained-html
* Support parallel execution with pytest-xdist.
* CI: GitHub Actions with parallel execution.
