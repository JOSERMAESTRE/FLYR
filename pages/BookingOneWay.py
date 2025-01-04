from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Base import Base


class BookingOneWay(Base):
    def __init__(self, driver):
        super().__init__(driver)  
        self.xpath_dropdown_Locator = "//button[contains(@class, 'dropdown_trigger')]"
        self.xpath_espaniol = "//button[span[contains(text(), 'Español')]]"
        self.POS_Locator = (By.ID, "pointOfSaleSelectorId")
        self.type_radio_locator = (By.XPATH, "//input[@id='journeytypeId_1']")
        self.origin_locator = (By.ID, "originDiv")
        self.destiny_locator = (By.XPATH, "//div[@class='control_field control_field-inbound is-focused']//div[@class='control_field_inner']")
        self.fly_date_locator = (By.XPATH, "//div[@class='control_fields date-control-oneway']")
        self.button_search = (By.ID, "searchButton")
    
    def search_fly(self, data):
        WebDriverWait(self.driver, 10).until(
         EC.invisibility_of_element((By.CLASS_NAME, "page-loader"))
        )
        wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(20)  
           
        dropdown_Locator = wait.until(EC.element_to_be_clickable((By.XPATH, self.xpath_dropdown_Locator)))
        dropdown_Locator.click()
        espaniol_button = wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath_espaniol)))
        espaniol_button.click()
        
        self.click(self.POS_Locator)
        posPopUp = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='points-of-sale points-of-sale--popup points-of-sale--opened']")))
        if posPopUp.is_displayed():
            buttons = self.driver.find_elements(By.XPATH, "//button[@class='points-of-sale_list_item_button']")
            buttons[5].click()
            self.click((By.XPATH, "//button[@class='button points-of-sale_footer_action_button']"))
            
        if data[0] == "Ida":
            self.click(self.type_radio_locator)
        
    
        self.click(self.origin_locator)
        self.sender("Valledupar", (By.XPATH, "//input[@placeholder='Origen']"))
        self.click((By.ID, "VUP"))

        destiny = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='control_options_type control_options_type--stations ng-star-inserted']")))
        if destiny.is_displayed():
            self.sender("Bogota", (By.XPATH, "//input[@placeholder='Hacia']"))
            self.click((By.ID, "BOG"))
        
       
        # Esperar y seleccionar una fecha
        date_picker = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='control_options ng-star-inserted']")))
        if date_picker.is_displayed():
            self.click((By.XPATH, "//div[contains(@aria-label,'31-1-2025')]"))
        
        # Esperar y manejar el número de pasajeros
        passenger = wait.until(EC.visibility_of_element_located((By.ID, "paxControlSearchId")))
        if passenger.is_displayed():
            plus_buttons = self.driver.find_elements(By.XPATH, "//div[@class='pax-control_selector_item_control']//button[@class='ui-num-ud_button plus']")
            for button in plus_buttons[1:]:
                 button.click()
            self.click((By.XPATH, "//button[@class='button control_options_selector_action_button']"))
        
        # Hacer clic en el botón de búsqueda
        self.click(self.button_search)
