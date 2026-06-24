import re
from playwright.sync_api import Page, expect

def test_example_domain(page: Page):
    # Navigate to example.com
    page.goto("https://example.com")

    # Assert that the page title contains "Example Domain"
    expect(page).to_have_title(re.compile("Example Domain"))

    # Assert that the main heading <h1> has the text "Example Domain"
    h1 = page.locator("h1")
    expect(h1).to_have_text("Example Domain")

    # Assert that the "Learn more" link is visible and has the correct URL
    more_info_link = page.locator("a", has_text="Learn more")
    expect(more_info_link).to_be_visible()
    expect(more_info_link).to_have_attribute("href", "https://iana.org/domains/example")
