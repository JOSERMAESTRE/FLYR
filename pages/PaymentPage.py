from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Base import Base
import time


class PaymentPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.confirm_Locator = (By.CSS_SELECTOR, "ds-button_label")
        self.CardOwner_Locator = (By.ID, "Holder")
        self.CardNumber_Locator = (By.ID, "Data")
        self.CardMonth_Locator = "expirationMonth_ExpirationDate"
        self.cardYear_Locator = "expirationYear_ExpirationDate"
        self.CVV_Locator = (By.ID, "Cvv")
        self.Email_Locator = (By.XPATH, "//input[@id='email']")
        self.Address_Locator = (By.ID, "address")
        self.City_Locator = (By.ID, "city")
        self.Country_Locator = "country"

    def pay(self):
        wait = WebDriverWait(self.driver, 10)
        cookie_button = wait.until(EC.visibility_of_element_located(
            (By.ID, "onetrust-accept-btn-handler")))
        cookie_button.click()

        iframe = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".payment-forms-layout_iframe"))
        )
        self.driver.switch_to.frame(iframe)
        time.sleep(5)
        self.sender("juan perez", self.CardOwner_Locator)
        self.sender("4111111111111111", self.CardNumber_Locator)
        self.click((By.ID, self.CardMonth_Locator))
        self.click((By.ID, self.CardMonth_Locator+"-2"))
        self.click((By.ID, self.cardYear_Locator))
        self.click((By.ID, self.cardYear_Locator+"-27"))
        self.sender("123", self.CVV_Locator)
        self.driver.switch_to.default_content()
        self.sender("jose.aja@gmail.com", self.Email_Locator)
        self.sender("calle 123", self.Address_Locator)
        self.sender("Bogota", self.City_Locator)
        self.click((By.ID, self.Country_Locator))
        self.click((By.ID, "country-42"))
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "terms"))
        )
        checkbox.click()
        confirm_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ds-btn-primary"))
        )
        confirm_button.click()
