from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class InventoryPage:

    products_title = By.CLASS_NAME, "title"
    app_logo = By.CLASS_NAME, "app_logo"
    burger_icon = By.ID, "react-burger-menu-btn"
    shopping_cart_icon = By.CLASS_NAME, "shopping_cart_link"
    inventory_list = By.CLASS_NAME, "inventory_list"
    inventory_item = By.CLASS_NAME, "inventory_item"
    logout_button = By.ID, "logout_sidebar_link"

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    # User is redirected to the Inventory page.
    # URL contains /inventory.html.
    def get_current_url(self) -> str:
        return self.driver.current_url
    
    # Page title displays Products.
    def get_product_title(self) -> str:
        return self.driver.find_element(*self.products_title).text
    
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
    def get_inventory_items(self) -> list[WebElement]:
        return self.driver.find_elements(*self.inventory_item)
    
    def open_menu(self) -> WebElement:
        self.driver.find_element(*self.burger_icon).click()

    # Logout option is available after opening the menu.
    def is_logout_option_visible(self) -> bool:
        return self.driver.find_element(*self.logout_button).is_displayed()
    

    
