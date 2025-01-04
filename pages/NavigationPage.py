from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Base import Base
import time


class NavigationPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def GoNavigationPage(self, link, link2):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.invisibility_of_element((By.CLASS_NAME, "page-loader"))
        )

        Barnav = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(),'"+link+"')]/ancestor::button")))
        Barnav.click()
        time.sleep(1)
        link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(),'"+link2+"')]/ancestor::a")))
        link.click()
        time.sleep(1)

    def VerifyNav(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element((By.CLASS_NAME, "page-loader")))
        return self.driver.title
