
from pages.login_page import LoginPage


def test_valid_login(driver_init):
    lp = LoginPage(driver_init)
    ip = lp.login("standard_user", "secret_sauce")
    # Verify URL
    assert "/inventory.html" in ip.get_current_url(), f"expected '/inventory.html' in url"
    # Verify page title
    assert ip.get_product_title() == "Products", "expected Products in the title"
    # Verify app logo
    assert ip.is_app_logo_visible(), "app logo is not visible"
    # Verify cart icon
    assert ip.is_shopping_cart_icon_visible(), "shopping cart icon is not visible"
    # Verify menu button
    assert ip.is_menu_bar_visible(), "Menu bar is invisible"
    # Verify inventory container
    assert ip.is_inventory_list_displayed(), "inventory container is not visible"
    # Verify inventory items count > 0
    assert len(ip.get_inventory_items()) > 0, "no Inventory items are present"    
    # Verify Logout link is displayed
    ip.open_menu()
    assert ip.is_logout_option_visible(), "logout menu is not visible"

