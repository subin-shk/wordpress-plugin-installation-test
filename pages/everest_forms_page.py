from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.everest_forms_locator import EverestFormsLocator


class EverestFormsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_nav_everest_forms(self):
        self.wait.until(
            EC.element_to_be_clickable(EverestFormsLocator.NAV_EVEREST_FORMS)
        ).click()
        
    def welcome_message(self):
      return self.wait.until(
        EC.visibility_of_element_located(EverestFormsLocator.WELCOME_TO_EVEREST)
      ).text
