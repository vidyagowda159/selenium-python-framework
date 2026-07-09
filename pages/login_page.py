from selenium.webdriver.common.by import By


class LoginPage:
    username_textbox = (By.XPATH, '//input[@id="user-name"]')
    password_textbox = (By.XPATH, '//input[@id="password"]')
    login_button = (By.XPATH, '//input[@id="login-button"]')

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()


    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
