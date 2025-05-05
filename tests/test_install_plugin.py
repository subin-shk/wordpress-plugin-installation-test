from pages.login_page import LoginPage

from pages.dashboard_page import DashboardPage

from pages.plugin_page import PluginPage
from pages.everest_forms_page import EverestFormsPage


class TestPlugin:
    def test_login(self, logged_in_driver, base_url):
        login = LoginPage(logged_in_driver, base_url)
        expected = "Welcome to WordPress!"
        actual = login.success_message()
        assert expected in actual, f"Failed: Expected {expected} to be part of {actual}"

    def test_go_to_plugin(self, logged_in_driver):
        dashboard = DashboardPage(logged_in_driver)

        dashboard.go_to_plugins()
        # expected = "Plugin"
        # actual = dashboard.plugin_title()
        # assert expected in actual, f"Failed: Expected {expected} to be part of {actual}"
        page_title = logged_in_driver.title
        assert (
            "Plugin" in page_title
        ), f"Expected 'Plugin' to be in the title, but got '{page_title}'"

    def test_add_new_plugin(self, logged_in_driver):
        self.test_go_to_plugin(logged_in_driver)
        plugin_page = PluginPage(logged_in_driver)
        plugin_page.add_plugin()
        page_title = logged_in_driver.title
        assert (
            "Add Plugins" in page_title
        ), f"Expected 'Add Plugins' to be in the title, but got '{page_title}'"

    def test_search_plugin(self, logged_in_driver):
        self.test_add_new_plugin(logged_in_driver)
        plugin_page = PluginPage(logged_in_driver)
        plugin_page.search_plugin("Everest Forms")
        assert (
            plugin_page.is_plugin_visible()
        ), "Failed: Everest Forms plugin was not found in the search results."

    def test_install_everest_forms(self, logged_in_driver):
        self.test_search_plugin(logged_in_driver)
        plugin_page = PluginPage(logged_in_driver)
        plugin_page.install_everest_forms()
        assert (
            plugin_page.wait_for_activate()
        ), "Failed: Everest Forms was not installed successfully"
        # plugin_page.click_activate()

    def test_click_activate(self, logged_in_driver):
        self.test_go_to_plugin(logged_in_driver)
        plugin_page = PluginPage(logged_in_driver)
        plugin_page.click_plugin_activate()

        actual = plugin_page.message()
        expected = "Plugin activated."
        assert expected in actual, "Failed: Plugin activation failed"

    def test_everest_forms_welcome_message(self, logged_in_driver):
        everest_page = EverestFormsPage(logged_in_driver)
        everest_page.click_nav_everest_forms()
        expected = "Welcome to Everest Forms!"
        actual = everest_page.welcome_message()
        assert expected in actual, "Failed: Couldn't navigate to Everest Forms"
