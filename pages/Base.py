from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Base:
    def __init__(self, driver=None):
        self.driver = driver

    def desktop_connection(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=options)
        return self.driver

    def find_element(self, value):
        return self.driver.find_element(*value)

    def click(self, value):
        self.driver.find_element(*value).click()

    def sender(self, text, value):
        self.driver.find_element(*value).send_keys(text)

    def go_to(self, url):
        self.driver.get(url)

    def is_displayed(self, by, value):
        try:
            return self.driver.find_element(by, value).is_displayed()
        except:
            return False
