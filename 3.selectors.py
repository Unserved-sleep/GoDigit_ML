from playwright.sync_api import sync_playwright
with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 1. locator()  page.loactor("#username") --id
                   #page.loactor(".login_btn") --class
                   #page.loactor("button") --tag
                   #page.locator("[name='username']") --attribute
    # 2. get_by_text()  page.get_by_text("Login").click() --visible text
    # 3. get_by_role()  page.get_by_role("button",name="Login").click()
                        #button textbox checkbox radio link heading
    # 4. get_by_label()  page.get_by_label("Username").fill("Admin")  --for forms
    # 5. get_by_placeholder()  page.get_by_placeholder("Enter Username").fill("Admin")
    # 6. get_by_title()   page.get_by_title("Login Button").click()
    # 7. get_by_test_id()   page.get_by_test_id("login-btn").click()
    # 8. CSS Selector
    # 9. XPath
    # 10. Chained Locators