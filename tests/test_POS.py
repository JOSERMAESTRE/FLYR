import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Base import Base
from pages.POSpage import Pospage


@pytest.fixture(scope="class")
def setup_and_teardown():
    base = Base(None)
    driver = base.desktop_connection()
    driver.maximize_window()
    base.go_to("https://nuxqa5.avtest.ink/")
    
    pospage = Pospage(driver)

    Pos_Ob = {
            "Otros países": "USD",
            "Chile": "USD",
            "España": "EUR"
    }
    
    yield pospage, Pos_Ob  

    driver.quit()


@pytest.mark.usefixtures("setup_and_teardown")
class TestLanguages:
    def test_POS(self, setup_and_teardown):
        pospage, Pos_Ob = setup_and_teardown
        
        for POS in Pos_Ob:
            pospage.search_Pos(POS)
   
