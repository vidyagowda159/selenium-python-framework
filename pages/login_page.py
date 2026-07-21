from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from .inventory_page import InventoryPage


class LoginPage:
    username_textbox = (By.ID, 'user-name')
    password_textbox = (By.ID, 'password')
    login_button = (By.ID, 'login-button')

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def enter_username(self, username: str) -> WebElement:
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password: str) -> WebElement:
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self) -> WebElement:
        self.driver.find_element(*self.login_button).click()

    def login(self, 
              username: str, 
              password: str) -> InventoryPage:
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return InventoryPage(self.driver)

