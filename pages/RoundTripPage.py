from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Base import Base
from .LanguagesPage import LanguagesPage
from .POSpage import Pospage
from .BookingOneWay import BookingOneWay
import time
class RoundTripPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.languaguesPage = LanguagesPage(driver)
        self.pOSpage = Pospage(driver)
        self.bookingOneWay = BookingOneWay(driver)
        self.type_radio_locator = (By.XPATH, "//input[@id='journeytypeId_0']")
        self.button_search = (By.ID, "searchButton")

        
    def search_fly(self, data):
        wait = WebDriverWait(self.driver, 10)
        self.languaguesPage.SelectLanguages("Español")
        self.pOSpage.search_Pos("Colombia")
        if data[0] == "Ida y vuelta":
            self.click(self.type_radio_locator)
            
        self.bookingOneWay.SelectWhereToGo(wait)
        self.bookingOneWay.SelectDateGo(wait)
        self.SelectDateBack(wait)
        self.bookingOneWay.SelectPassengers(wait)
        self.click(self.button_search)
        
    def SelectDateBack(self,wait):
        date_picker = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='control_options ng-star-inserted']")))
        if date_picker.is_displayed():
            self.click((By.XPATH, "//div[contains(@aria-label,'28-2-2025')]"))
        
        
        