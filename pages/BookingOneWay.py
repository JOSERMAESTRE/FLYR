from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .LanguagesPage import LanguagesPage
from .POSpage import Pospage
from .Base import Base


class BookingOneWay(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.languaguesPage = LanguagesPage(driver)
        self.pOSpage = Pospage(driver)
        self.type_radio_locator = (By.XPATH, "//input[@id='journeytypeId_1']")
        self.origin_locator = (By.ID, "originDiv")
        self.destiny_locator = (
            By.XPATH, "//div[@class='control_field control_field-inbound is-focused']//div[@class='control_field_inner']")
        self.fly_date_locator = (
            By.XPATH, "//div[@class='control_fields date-control-oneway']")
        self.button_search = (By.ID, "searchButton")

    def search_fly(self, data):
        wait = WebDriverWait(self.driver, 10)
        self.languaguesPage.SelectLanguages("Español")
        self.pOSpage.search_Pos("Colombia")
        self.driver.implicitly_wait(5)
        if data[0] == "Ida":
            self.click(self.type_radio_locator)

        self.SelectWhereToGo(wait)

        # Esperar y seleccionar una fecha
        self.SelectDateGo(wait)

        # Esperar y manejar el número de pasajeros
        self.SelectPassengers(wait)
        
        # Hacer clic en el botón de búsqueda
        self.click(self.button_search)
    
    def SelectWhereToGo(self,wait):
        self.click(self.origin_locator)
        self.sender("Valledupar", (By.XPATH, "//input[@placeholder='Origen']"))
        self.click((By.ID, "VUP"))

        destiny = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='control_options_type control_options_type--stations ng-star-inserted']")))
        if destiny.is_displayed():
            self.sender("Bogota", (By.XPATH, "//input[@placeholder='Hacia']"))
            self.click((By.ID, "BOG"))
    
    def SelectDateGo(self,wait):
         date_picker = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='control_options ng-star-inserted']")))
         if date_picker.is_displayed():
            self.click((By.XPATH, "//div[contains(@aria-label,'28-1-2025')]"))
            
            
    def SelectPassengers(self,wait):
         passenger = wait.until(EC.visibility_of_element_located(
            (By.ID, "paxControlSearchId")))
         if passenger.is_displayed():
            plus_buttons = self.driver.find_elements(
                By.XPATH, "//div[@class='pax-control_selector_item_control']//button[@class='ui-num-ud_button plus']")
            for button in plus_buttons[1:]:
                button.click()
            self.click(
                (By.XPATH, "//button[@class='button control_options_selector_action_button']"))
