from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.dashboard_locator import DashboardLocator


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self):
        self.wait.until(EC.title_contains("Dashboard"))
        return "Dashboard" in self.driver.title

    def go_to_plugins(self):
        self.wait.until(
            EC.element_to_be_clickable(DashboardLocator.PLUGINS_MENU)
        ).click()
        
    def plugin_title(self):
        msg = self.wait.until(
            EC.presence_of_element_located(DashboardLocator.PLUGIN_TITLE)
        ).text
        return msg
