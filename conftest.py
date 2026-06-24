import base64
import os
import pytest
from playwright.sync_api import Page

@pytest.fixture(autouse=True)
def capture_trace(context):
    """
    Fixture to automatically capture Playwright trace and save it to traces/trace.zip
    """
    os.makedirs("traces", exist_ok=True)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield
    context.tracing.stop(path="traces/trace.zip")


@pytest.fixture(autouse=True)
def mock_login_pages(page: Page):
    """
    Autouse fixture to intercept navigation to https://example.com/login 
    and serve a mock single-page application that handles login, dashboard redirection,
    and invalid credential errors.
    """
    def handle_login_route(route):
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Login - Example Domain</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                .form-group { margin-bottom: 15px; }
                label { display: block; margin-bottom: 5px; font-weight: bold; }
                input { width: 250px; padding: 8px; border: 1px solid #ccc; border-radius: 4px; }
                button { padding: 8px 15px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; }
                button:hover { background-color: #0056b3; }
                .error { color: #dc3545; display: none; margin-top: 15px; font-weight: bold; }
                .success { display: none; }
                #logoutBtn { background-color: #6c757d; }
                #logoutBtn:hover { background-color: #5a6268; }
            </style>
        </head>
        <body>
            <div id="loginSection">
                <h1>Login</h1>
                <form id="loginForm" onsubmit="event.preventDefault(); handleLogin();">
                    <div class="form-group">
                        <label for="username">Username</label>
                        <input type="text" id="username" placeholder="Enter username" required />
                    </div>
                    <div class="form-group">
                        <label for="password">Password</label>
                        <input type="password" id="password" placeholder="Enter password" required />
                    </div>
                    <button type="submit" id="loginBtn">Login</button>
                </form>
                <div id="errorMsg" class="error">Invalid username or password</div>
            </div>

            <div id="dashboardSection" class="success">
                <h1>Dashboard</h1>
                <p id="welcomeMsg">Welcome, admin!</p>
                <button id="logoutBtn" onclick="handleLogout()">Logout</button>
            </div>

            <script>
                function handleLogin() {
                    const user = document.getElementById('username').value;
                    const pass = document.getElementById('password').value;
                    const errorEl = document.getElementById('errorMsg');
                    const loginEl = document.getElementById('loginSection');
                    const dashEl = document.getElementById('dashboardSection');
                    
                    if (user === 'admin' && pass === 'admin123') {
                        errorEl.style.display = 'none';
                        loginEl.style.display = 'none';
                        dashEl.style.display = 'block';
                    } else {
                        errorEl.style.display = 'block';
                    }
                }

                function handleLogout() {
                    document.getElementById('username').value = '';
                    document.getElementById('password').value = '';
                    document.getElementById('errorMsg').style.display = 'none';
                    document.getElementById('loginSection').style.display = 'block';
                    document.getElementById('dashboardSection').style.display = 'none';
                }
            </script>
        </body>
        </html>
        """
        route.fulfill(status=200, content_type="text/html", body=html_content)

    # Intercept calls to example.com/login and any routes containing example.com/login
    page.route("**/example.com/login", handle_login_route)
    page.route("https://example.com/login", handle_login_route)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture a screenshot on test failure and embed it in the HTML report.
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        # Check if the 'page' fixture is active in the test
        if "page" in item.funcargs:
            page: Page = item.funcargs["page"]
            try:
                # Capture screenshot as a base64 encoded string
                screenshot_bytes = page.screenshot(timeout=5000)
                screenshot_base64 = base64.b64encode(screenshot_bytes).decode("utf-8")
                
                # Embed the image in the HTML report
                html_image = f'<div style="margin-top: 10px;"><img src="data:image/png;base64,{screenshot_base64}" alt="screenshot" style="width:600px;border:1px solid #ccc;"/></div>'
                extra.append(pytest_html.extras.html(html_image))
            except Exception as e:
                print(f"\n[Warning] Failed to capture screenshot for HTML report: {e}")
        report.extra = extra
