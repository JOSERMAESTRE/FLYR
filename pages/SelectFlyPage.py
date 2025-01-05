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
        self.second_price_Locator = (
            By.CSS_SELECTOR, ".journey_price_button ng-tns-c12-20 ng-star-inserted")
        self.fee_Locator = (By.CSS_SELECTOR, ".fare_button")
        self.confirm_Locator = (
            By.CSS_SELECTOR, "button.page_button .button_label")

    def select_fly(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element((By.CLASS_NAME, "page-loader"))
        )
        self.click(self.filter_Locator)
        buttonsprice = self.driver.find_elements(*self.price_Locator)
        buttonsprice[0].click()
        wait = WebDriverWait(self.driver, 10)

        button_fee = wait.until(EC.element_to_be_clickable(self.fee_Locator))

        button_fee.click()

    def select_fly_Back(self):

        wait = WebDriverWait(self.driver, 20)
        wait.until(
            EC.invisibility_of_element((By.CLASS_NAME, "page-loader"))
        )
        button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".journey_price_button.ng-tns-c12-20.ng-star-inserted"))
        )

        # Desplazar al elemento
        self.driver.execute_script("arguments[0].click();", button)

        # Hacer clic en el botón
        
        buttons_fee = WebDriverWait(self.driver, 20).until(
        EC.presence_of_all_elements_located(self.fee_Locator)
        )
    
         # Esperar a que el tercer botón sea clickeable
        button_to_click = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(buttons_fee[2])
        )
        
        # Hacer clic en el tercer botón
        button_to_click.click()

    def confirm_fly(self):
        time.sleep(5)
        if (self.driver.title.__contains__("Seleccionar vuelo")):
            self.click(self.confirm_Locator)
