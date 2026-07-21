from selenium.webdriver.common.by import By
# from selenium.webdriver.common.webdriver


class InventoryPage:

    products_title = By.CLASS_NAME, "title"
    app_logo = By.CLASS_NAME, "app_logo"
    burger_icon = By.ID, "react-burger-menu-btn"
    shopping_cart_icon = By.CLASS_NAME, "shopping_cart_link"
    inventory_list = By.CLASS_NAME, "inventory_list"
    inventory_item = By.CLASS_NAME, "inventory_item"
    logout_button = By.ID, "logout_sidebar_link"

    def __init__(self, driver):
        self.driver = driver

    # User is redirected to the Inventory page.
    # URL contains /inventory.html.
    def is_url_valid(self) -> bool:
        return "/inventory.html" in self.driver.current_url
    
    # Page title displays Products.
    def is_product_title_displayed(self) -> bool:
        return self.driver.find_element(*self.products_title).is_displayed()
    
    # Burger (menu) button is visible.
    def is_menu_bar_visible(self) -> bool:
        return self.driver.find_element(*self.burger_icon).is_displayed()
    
    # Shopping cart icon is visible.
    def is_shopping_cart_icon_visible(self) -> bool:
        return self.driver.find_element(*self.shopping_cart_icon).is_displayed()
    
    # App logo is visible.
    def is_app_logo_visible(self) -> bool:
        return self.driver.find_element(*self.app_logo).is_displayed()
    
    # Inventory list is displayed.
    def is_inventory_list_displayed(self) -> bool:
        return self.driver.find_element(*self.inventory_list).is_displayed()
    
    # At least one inventory item is present.
    def get_inventory_items(self):
        return self.driver.find_elements(*self.inventory_item)
    
    def open_menu(self) -> None:
        self.driver.find_element(*self.burger_icon).click()

    # Logout option is available after opening the menu.
    def is_logout_option_visible(self)->bool:
        self.open_menu()
        return self.driver.find_element(*self.logout_button).is_displayed()
    

    
