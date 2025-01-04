from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Base import Base


class Pospage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.POS_Locator = (By.ID, "pointOfSaleSelectorId")

    def search_Pos(self, POS):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element((By.CLASS_NAME, "page-loader"))
        )
        wait = WebDriverWait(self.driver, 10)
        element = self.driver.find_element(By.ID, "pointOfSaleSelectorId")
        self.driver.execute_script("arguments[0].click();", element)

        posPopUp = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='points-of-sale points-of-sale--popup points-of-sale--opened']")))
        if posPopUp.is_displayed():
            button = self.driver.find_element(
                By.XPATH, "//button[@class='points-of-sale_list_item_button']//span[contains(text(),'"+POS+"')]")
            button.click()
            self.click(
                (By.XPATH, "//button[@class='button points-of-sale_footer_action_button']"))

    def VerifyPos(self, POS):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element((By.CLASS_NAME, "page-loader"))
        )
        ResultPOS = self.driver.find_ResultPOS(
            By.XPATH, "//*[contains(text(),'"+POS+"')]")
        if len(ResultPOS) > 0:
            return True
        else:
            return False
