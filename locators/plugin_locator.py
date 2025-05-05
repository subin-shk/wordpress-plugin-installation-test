from selenium.webdriver.common.by import By


class PluginLocator:
    ADD_NEW_PLUGIN = (By.CLASS_NAME, "page-title-action")
    SEARCH_PLUGIN = (By.ID, "search-plugins")
    EVEREST_PLUGIN_TITLE = (By.XPATH, "//h3/a[contains(text(), 'Everest Forms')]")

    INSTALL = (
        By.XPATH,
        "//h3/a[contains(text(), 'Everest Forms')]/following::a[contains(@class,'install-now')]",
    )
    ACTIVATE_BUTTON = (
        By.XPATH,
        "//h3/a[contains(text(), 'Everest Forms')]/following::a[contains(text(),'Activate')]",
    )
    MESSAGE = (By.ID, "message")
    PLUGIN_ACTIVATE = (
        By.XPATH,
        "//tr[.//strong[contains(text(), 'Everest Forms')]]//a[normalize-space()='Activate']",
    )

    INSTALL_BUTTON = (By.XPATH, "//a[contains(text(), 'Install Now')]")

    
