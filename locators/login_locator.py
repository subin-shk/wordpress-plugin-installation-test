from selenium.webdriver.common.by import By


class LoginLocator:
    USERNAME = (By.ID, "user_login")
    PASSWORD = (By.ID, "user_pass")
    LOGIN_BUTTON = (By.ID, "wp-submit")
    WELCOME_MESSAGE = (By.CLASS_NAME, "welcome-panel-header")
