from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Base import Base
import time


class SelectflyPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.filter_Locator = (By.CSS_SELECTOR, ".filters-control_button")
        self.price_Locator = (By.CSS_SELECTOR, ".journey_price")
        self.fee_Locator = (By.CSS_SELECTOR, ".fare_button")
        self.confirm_Locator = (
            By.CSS_SELECTOR, "button.page_button .button_label")

    def select_fly(self):
        self.click(self.filter_Locator)
        buttonsprice = self.driver.find_elements(*self.price_Locator)
        buttonsprice[0].click()
        wait = WebDriverWait(self.driver, 10)

        button_fee = wait.until(EC.element_to_be_clickable(self.fee_Locator))

        button_fee.click()
        time.sleep(5)
        if (self.driver.title.__contains__("Seleccionar vuelo")):
            self.click(self.confirm_Locator)
