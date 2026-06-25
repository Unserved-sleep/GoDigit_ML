from pages.login_page import LoginPage
import pytest

@pytest.mark.parametrize(
"username,password,success",
    [
        ("standard_user", "secret_sauce", True),
        ("locked_out_user", "secret_sauce", False),
        ("problem_user", "secret_sauce", True),
    ]
)

def test_login_page(page, username, password, success):
    login = LoginPage(page)
    login.open_login_page()
    login.login(username, password)

    if success:
        assert page.url == "https://www.saucedemo.com/inventory.html"
    else:
        assert page.url != "https://www.saucedemo.com/inventory.html"