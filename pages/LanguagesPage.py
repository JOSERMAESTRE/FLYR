from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .Base import Base

class LanguagesPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.Language_Locator = "//button[contains(@class, 'dropdown_trigger')]"

        
    def SelectLanguages(self, language):
        WebDriverWait(self.driver, 10).until(
         EC.invisibility_of_element((By.CLASS_NAME, "page-loader"))
        )
        wait = WebDriverWait(self.driver, 10)
        dropdown_Locator = wait.until(EC.element_to_be_clickable((By.XPATH, self.Language_Locator)))
        dropdown_Locator.click()
        languageButton = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[span[contains(text(), '"+language+"')]]")))
        languageButton.click()
        
    def VerifyLanguage(self):
        WebDriverWait(self.driver, 10).until(
         EC.invisibility_of_element((By.CLASS_NAME, "page-loader"))
        )
        return self.driver.title 
        
       