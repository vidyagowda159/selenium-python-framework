from pages.login_page import LoginPage


def test_login(driver_init):
    lp = LoginPage(driver_init)
    lp.login("standard_user", "secret_sauce")
