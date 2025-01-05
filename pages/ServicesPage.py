from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Base import Base
import time


class ServicesPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.confirm_Locator = "button.page_button .button_label"
        self.Continue_Locator = "button.page_button"

    def Confirm(self):
        WebDriverWait(self.driver, 30).until(
            EC.title_is("avianca - Servicios")
        )

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element(
                (By.CSS_SELECTOR, ".page-loader"))
        )

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.Continue_Locator)))
        self.driver.find_element(By.CSS_SELECTOR, self.Continue_Locator).click()
        
    def SelectServices(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(
            EC.invisibility_of_element(
                (By.CSS_SELECTOR, ".page-loader"))
        )
        
        add_button = wait.until(
            EC.element_to_be_clickable((By.ID, "serviceButtonTypeBusinessLounge"))
        )
        add_button.click()
        
        wait = WebDriverWait(self.driver, 20)  # Tiempo de espera de 20 segundos
        modal_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "modal-content")))
        
        if modal_element.is_displayed():
            add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@role='button']")))

            add_button.click()
            
            confirm_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".amount-summary_button.amount-summary_button-action.is-action")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", confirm_button)
            confirm_button.click()
  
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.Continue_Locator)))
        self.driver.find_element(By.CSS_SELECTOR, self.Continue_Locator).click()

            
