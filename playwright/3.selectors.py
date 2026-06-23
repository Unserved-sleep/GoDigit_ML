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
    # 8. CSS Selector  locators - class, id, name, attributes,
                        # page.locator(
                        # "div button"
                        # ).click()   child selectors
    # 9. XPath   page.locator("//button[text()='Login']")
    # 10. Chained Locators  # page.locator(
                            # "#login-form"
                            # ).get_by_role(
                            # "button",
                            # name="Login"
                            # ).click()

    # Multiple matching elements
    # page.get_by_text(
    #     "Delete"
    # ).first.click()  .last.click()   .nth(1).click

    # role - label - placeholder - id - xpath

    # Auto-wait - default timeout -30secs
        # page.set_default_timeout(
        # 60000
        # )
    # for specific
        # page.set_default_timeout(60000)
    # with assertions
        # expect(
        # page.get_by_text(
        # "Login Successful"
        # )
        # ).to_be_visible()

    # specific waits
    # .wait_for(state="visible")  or hidden
    # page.wait_for_url("**/dashboard")
    # page.wait_for_load_state() -- domcontentloaded load networkidle


    # for api response
        # with page.expect_response(
        # "**/users"
        # ):
        #     page.click(
        #     "#loadUsers"
        #     )

        # with page.expect_request(
        # "**/users"
        # ):
        #     page.click(
        #     "#loadUsers"
        #     )


