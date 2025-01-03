from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Base import Base
import time

class PassengersPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.AdultGender_Locator = "IdPaxGender_7E7E303030312D30312D30317E353334423438324433323244343535383534"
        self.AdultFirsName_Locator = (By.ID, "IdFirstName7E7E303030312D30312D30317E353334423438324433323244343535383534")
        self.AdultLastName_Locator = (By.ID, "IdLastName7E7E303030312D30312D30317E353334423438324433323244343535383534")
        self.AdultBirthDateDayLocator = "dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433323244343535383534_"
        self.AdultBirthDateMonthLocator = "dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433323244343535383534_"
        self.AdultBirthDateYearLocator = "dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433323244343535383534_"
        self.AdultnacionalityLocator = "IdDocNationality_7E7E303030312D30312D30317E353334423438324433323244343535383534"
        self.customerGramsLocator = "customerPrograms"
        
        self.BabyGender_Locator = "IdPaxGender_7E7E303030312D30312D30317E353334423438324433313244343535383534"
        self.BabyFirsName_Locator = (By.ID, "IdFirstName7E7E303030312D30312D30317E353334423438324433313244343535383534")
        self.BabyLastName_Locator = (By.ID, "IdLastName7E7E303030312D30312D30317E353334423438324433313244343535383534")
        self.BabyBirthDateDayLocator = "dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433313244343535383534_"
        self.BabyBirthDateMonthLocator = "dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433313244343535383534_"
        self.BabyBirthDateYearLocator = "dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433313244343535383534_"
        self.BabynacionalityLocator = "IdDocNationality_7E7E303030312D30312D30317E353334423438324433313244343535383534"
        
        
        
    def AdultData(self, data):

        if data[0]=="Masculino":
            wait = WebDriverWait(self.driver, 10)
            dropdown_button = wait.until(EC.element_to_be_clickable((By.ID, self.AdultGender_Locator)))
            dropdown_button.click()
            
            options = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".ui-dropdown_item")))
            for option in options:
                if option.text.strip() == "Masculino": 
                    option.click()
                    break

        # Fill out first name, last name, and birthdate
        self.sender(data[1], self.AdultFirsName_Locator)
        self.sender(data[2], self.AdultLastName_Locator) 
      
        self.click((By.ID, self.AdultBirthDateDayLocator))
        self.click((By.XPATH, "//span[text()='"+data[3]+"']"))
        self.click((By.ID, self.AdultBirthDateMonthLocator))
        self.click((By.XPATH, "//span[text()='"+data[4]+"']"))
        self.click((By.ID, self.AdultBirthDateYearLocator))
        self.click((By.XPATH, "//span[text()='"+data[5]+"']"))
        self.click((By.ID, self.AdultnacionalityLocator))
        self.click((By.XPATH, "//span[text()='"+data[6]+"']"))
        self.click((By.ID, self.customerGramsLocator))
        self.click((By.XPATH, "//span[text()='"+data[7]+"']"))
      
    def BabyData(self, DataBaBy):
          if DataBaBy[0]=="Masculino":
            wait = WebDriverWait(self.driver, 10)
            dropdown_button = wait.until(EC.element_to_be_clickable((By.ID, self.BabyGender_Locator)))
            dropdown_button.click()
            
            options = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".ui-dropdown_item")))
            for option in options:
                if option.text.strip() == "Masculino": 
                    option.click()
                    break
       
            self.sender(DataBaBy[1], self.BabyFirsName_Locator)
            self.sender(DataBaBy[2], self.BabyLastName_Locator)
      
            self.click((By.ID, self.BabyBirthDateDayLocator))
            self.click((By.XPATH, "//span[text()='"+DataBaBy[3]+"']"))
            self.click((By.ID, self.BabyBirthDateMonthLocator))
            self.click((By.XPATH, "//span[text()='"+DataBaBy[4]+"']"))
            self.click((By.ID, self.BabyBirthDateYearLocator))
            self.click((By.XPATH, "//span[text()='"+DataBaBy[5]+"']"))
            self.click((By.ID, self.BabynacionalityLocator))
            self.click((By.ID, self.BabynacionalityLocator+"-0"))
                
            time.sleep(12)
            