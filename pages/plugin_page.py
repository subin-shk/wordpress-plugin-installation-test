from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.plugin_locator import PluginLocator
from selenium.webdriver.common.keys import Keys


class PluginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def add_plugin(self):
        self.wait.until(
            EC.element_to_be_clickable(PluginLocator.ADD_NEW_PLUGIN)
        ).click()

    def search_plugin(self, term):
        self.wait.until(
            EC.presence_of_element_located(PluginLocator.SEARCH_PLUGIN)
        ).send_keys(term + Keys.ENTER)

    def is_plugin_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(PluginLocator.EVEREST_PLUGIN_TITLE)
        )

    def install_everest_forms(self):
        self.wait.until(EC.element_to_be_clickable(PluginLocator.INSTALL)).click()

    def wait_for_activate(self):
        try:
            return (
                self.wait.until(
                    EC.text_to_be_present_in_element(PluginLocator.INSTALL, "Installed")
                )
                is not None
            )
        except TimeoutError:
            return False

    def click_activate(self):
        self.wait.until(
            EC.element_to_be_clickable(PluginLocator.ACTIVATE_BUTTON)
        ).click()

    def message(self):
        return self.wait.until(
            EC.presence_of_element_located(PluginLocator.MESSAGE)
        ).text

    def click_plugin_activate(self):
        self.wait.until(
            EC.element_to_be_clickable(PluginLocator.PLUGIN_ACTIVATE)
        ).click()
