from playwright.sync_api import sync_playwright

with (sync_playwright() as p):
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://the-internet.herokuapp.com")

    title = page.title()
    print(title)
    # verify title
    assert title == "The Internet"
    print("Title verified")
    # page url
    page.get_by_text("Form Authentication").click()
    assert page.url == "https://the-internet.herokuapp.com/login"
    print("URL verified")
    # login test
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button")
    assert "secure" in page.url
    print("Login successful")
    #verify text
    message = page.locator("#flash").text_content()
    assert "You logged into a secure area!" in message
    print("Verified Text")
    #verify element
    logout_btn = page.locator(".button")
    assert logout_btn.is_visible()
    logout_btn.click()
    assert page.url == "https://the-internet.herokuapp.com/login"
    print("Logout successful")
    #checkbox test
    page.goto("https://the-internet.herokuapp.com")
    page.get_by_text("Checkboxes").click()
    checkbox1 = page.locator("input").nth(0)
    checkbox1.check()
    assert checkbox1.is_checked()
    print("Checkboxes checked")
    checkbox2 = page.locator("#checkboxes").get_by_role("checkbox").nth(1)
    checkbox2.uncheck()
    assert not checkbox2.is_checked()
    print("Checkboxes unchecked")
    page.go_back()
    #dropdown test
    page.get_by_text("Dropdown").click()
    page.select_option("#dropdown","1")
    selected = page.locator("#dropdown").input_value()
    assert selected == "1"
    print("Selected dropdown")
    # Count
    page.go_back()
    page.get_by_text("Add/Remove Elements").click()
    page.click("text=Add Element")
    page.click("text=Add Element")
    page.click("text=Add Element")
    buttons = page.locator("text=Delete")
    assert buttons.count() == 3
    print("counted")
    #link texts
    page.go_back()
    links = page.locator("li")
    for i in range(links.count()):
        print(links.nth(i).text_content())