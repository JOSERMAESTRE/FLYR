from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Base import Base


class ServicesPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.confirm_Locator = "button.page_button .button_label"

    def Confirm(self):
        WebDriverWait(self.driver, 30).until(
            EC.title_is("avianca - Servicios")
        )

        WebDriverWait(self.driver, 3).until(
            EC.invisibility_of_element(
                (By.CSS_SELECTOR, ".page-loader ng-star-inserted"))
        )

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, self.confirm_Locator))
        )

        self.driver.find_element(By.CSS_SELECTOR, self.confirm_Locator).click()
