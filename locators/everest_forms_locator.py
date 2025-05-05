from selenium.webdriver.common.by import By


class EverestFormsLocator:
    NAV_EVEREST_FORMS = (
        By.XPATH,
        "//div[@class='wp-menu-name' and contains(text(),'Everest Forms')]",
    )
    WELCOME_TO_EVEREST = (By.XPATH, "//h3[@class='chakra-heading css-zno0g5']")