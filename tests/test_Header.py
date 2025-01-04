import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Base import Base
from pages.NavigationPage import NavigationPage
from pages.LanguagesPage import LanguagesPage
import time

@pytest.fixture(scope="class")
def setup_and_teardown():
    base = Base(None)
    driver = base.desktop_connection()
    driver.maximize_window()
    base.go_to("https://nuxqa5.avtest.ink/")
    
    navigationPage = NavigationPage(driver)
    languagesPage = LanguagesPage(driver)

    options = {
            "Español": ["lifemiles", "Programa lifemiles","avianca - Programa lifemiles"],
            "English": ["Your booking", "Online check-in","avianca - Check-in online"],
            "Français": ["Offres et destinations", "Visites et excursions","Civitatis – Visites guidées et excursions dans le monde entier"],
                               
        }
    
    yield navigationPage, languagesPage, options  

    driver.quit()


@pytest.mark.usefixtures("setup_and_teardown")
class TestHeader:
    def test_Header(self, setup_and_teardown):
        navigationPage, languagesPage, options= setup_and_teardown
       
        for language, links in options.items():
            languagesPage.SelectLanguages(language)
            navigationPage.GoNavigationPage(links[0],links[1])
            assert navigationPage.VerifyNav().strip() == links[2].strip()

            
   
