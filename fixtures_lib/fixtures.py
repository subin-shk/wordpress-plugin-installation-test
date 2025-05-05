import pytest
from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os


# Provide the base URL for the WordPress site
@pytest.fixture(scope="session")
def base_url():
    return "http://localhost/wordpress"


# Provide the WebDriver instance for the test
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


# To haandle login
@pytest.fixture
def logged_in_driver(driver, base_url):
    load_dotenv()
    username = os.getenv("WP_USERNAME")
    password = os.getenv("WP_PASSWORD")
    login_page = LoginPage(driver, base_url)
    login_page.load()
    login_page.login(username, password)
    expected = "Welcome to WordPress!"
    actual = login_page.success_message()
    assert expected in actual, f"Failed: Expected {expected} to be part of {actual}"
    return driver
