from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Base import Base
import time

class FooterPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def GoFooterPage(self,link):
        WebDriverWait(self.driver, 10).until(
         EC.invisibility_of_element((By.CLASS_NAME, "page-loader"))
        )
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        footer = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'" + link + "')]")))
        footer.click()
        
    def VerifyFooter(self):
        WebDriverWait(self.driver, 10).until(
         EC.invisibility_of_element((By.CLASS_NAME, "page-loader"))
        )
        return self.driver.title
    
        
      