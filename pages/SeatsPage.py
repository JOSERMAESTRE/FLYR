from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from .Base import Base


class SeatsPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.confirm_Locator = (
            By.XPATH, "//button[contains(@class, 'amount-summary_button') and contains(@class, 'amount-summary_button-action')]//span")

    def chooseseats(self):
        WebDriverWait(self.driver, 30).until(
            EC.title_is("avianca - Seleccionar asiento")
        )

        seat_button1 = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(text(), '15A')]/ancestor::button"))
        )
        self.driver.execute_script("arguments[0].click();", seat_button1)

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element(
                (By.CSS_SELECTOR, ".page-loader"))
        )
        seat_button2 = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(text(), '15B')]/ancestor::button"))
        )
        self.driver.execute_script("arguments[0].click();", seat_button2)

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element(
                (By.CSS_SELECTOR, ".page-loader"))
        )
        seat_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(text(), '15C')]/ancestor::button"))
        )
        self.driver.execute_script("arguments[0].click();", seat_button)

        time.sleep(5)

    def Confirm(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.confirm_Locator)
        )
        self.driver.find_element(*self.confirm_Locator).click()
