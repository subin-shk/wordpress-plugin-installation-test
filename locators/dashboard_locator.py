from selenium.webdriver.common.by import By


class DashboardLocator:
    PLUGINS_MENU = (By.ID, "menu-plugins")
    PLUGIN_TITLE = (By.CLASS_NAME, "wp-heading-inline")
    
