from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from .Base import Base


class ComfirmationPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def Confirmation(self):
        wait = WebDriverWait(self.driver, 50)
        message_element = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "span.action-message_title-text")))

        # Obtén el mensaje
        message = message_element.text
        return message
