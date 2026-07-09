import time
from selenium import webdriver
from pytest import fixture
from config.config import Config


@fixture()
def driver_init():
    if Config.BROWSER.lower() == "chrome":
        c_options = webdriver.ChromeOptions()
        c_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=c_options)

    elif Config.BROWSER.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    driver.implicitly_wait(30)
    driver.get(Config.BASE_URL)
    driver.maximize_window()

    yield driver
    title = driver.title
    print(title)
    # driver.quit()



