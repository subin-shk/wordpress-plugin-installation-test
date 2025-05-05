from locators.login_locator import LoginLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.base_url = base_url

    def load(self):
        self.driver.get(f"{self.base_url}/wp-login.php")
        self.wait.until(EC.title_contains("Log In"))

    def login(self, username, password):
        self.wait.until(
            EC.visibility_of_element_located(LoginLocator.USERNAME)
        ).send_keys(username)
        self.wait.until(
            EC.visibility_of_element_located(LoginLocator.PASSWORD)
        ).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(LoginLocator.LOGIN_BUTTON)).click()

    def success_message(self):
        msg = self.wait.until(
            EC.presence_of_element_located(LoginLocator.WELCOME_MESSAGE)
        ).text
        return msg
