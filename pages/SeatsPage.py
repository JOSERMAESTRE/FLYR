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
        self.PlaneBack_locator = (
            By.XPATH, "//button[starts-with(@id, '424F477')]")

    def chooseseats(self, seats):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.title_is("avianca - Seleccionar asiento")
            )
            for seat in seats:
                seat_button = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, f"//span[contains(text(), '{seat}')]/ancestor::button")
                    )
                )
                self.close_modal()
                self.driver.execute_script("arguments[0].click();", seat_button)
                WebDriverWait(self.driver, 10).until(EC.invisibility_of_element((By.CSS_SELECTOR, ".page-loader")))
                self.close_modal()
        except Exception as e:
            print(f"Ocurrió un error al seleccionar los asientos: {e}")

    def chooseseatsBack(self, seats):
        try:
            SecondPlane = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.PlaneBack_locator)
            )
            self.driver.execute_script("arguments[0].click();", SecondPlane)
            
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element((By.CSS_SELECTOR, ".page-loader"))
            )

            for seat in seats:
                seat_button = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, f"//span[contains(text(), '{seat}')]/ancestor::button")
                    )
                )
                
                self.close_modal()
                self.driver.execute_script("arguments[0].click();", seat_button)
                WebDriverWait(self.driver, 10).until(
                    EC.invisibility_of_element((By.CSS_SELECTOR, ".page-loader"))
                )
                self.close_modal()
        except Exception as e:
            print(f"Ocurrió un error al seleccionar los asientos en el segundo avión: {e}")


    def Confirm(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.confirm_Locator)
        )
        self.driver.find_element(*self.confirm_Locator).click()

    def close_modal(self):
        try:
            modal = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "modal-dialog"))
            )
            close_button = modal.find_element(By.XPATH, "//button[@data-dismiss='modal']")
            close_button.click()
            print("Modal cerrado exitosamente.")
        except Exception as e:
            print(f"No se pudo cerrar el modal: {e}")
