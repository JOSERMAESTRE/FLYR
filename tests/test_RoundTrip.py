import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.ComfirmationPage import ComfirmationPage
from pages.PaymentPage import PaymentPage
from pages.SeatsPage import SeatsPage
from pages.ServicesPage import ServicesPage
from pages.Base import Base
from pages.PassengersPage import PassengersPage
from pages.SelectFlyPage import SelectflyPage
from selenium.webdriver.support import expected_conditions as EC
from pages.BookingOneWay import BookingOneWay
from pages.RoundTripPage import RoundTripPage
import time



# Definición del fixture
@pytest.fixture(scope="class")
def setup_and_teardown():
    base = Base(None)
    driver = base.desktop_connection()
    driver.maximize_window()
    base.go_to("https://nuxqa5.avtest.ink/")

    roundTripPage = RoundTripPage(driver)
    selectFlyPage = SelectflyPage(driver)
    passengersPage = PassengersPage(driver)
    servicesPage = ServicesPage(driver)
    seatsPage = SeatsPage(driver)
    paymentPage = PaymentPage(driver)
    yield roundTripPage, selectFlyPage,passengersPage, servicesPage, seatsPage,paymentPage

    # Cerrar el WebDriver después de la prueba
    driver.quit()

# Definición de la clase de prueba
@pytest.mark.usefixtures("setup_and_teardown")
class TestRoundTrip:

    def test_round_trip(self, setup_and_teardown):
        roundTripPage,selectFlyPage,passengersPage,servicesPage,seatsPage,paymentPage = setup_and_teardown
        data = ["Ida y vuelta"]
        roundTripPage.search_fly(data)
        selectFlyPage.select_fly()
        selectFlyPage.select_fly_Back()
        selectFlyPage.confirm_fly()
        dataAdult = ["Masculino", "Jose", "Maestre",
                     "20", "10", "1993", "Colombia", "No aplica"]
        passengersPage.AdultData(dataAdult)

        dataBaby = ["Masculino", "Juan", "Maestre",
                    "15", "12", "2024", "Colombia"]
        passengersPage.BabyData(dataBaby)

        dataTeen = ["Femenino", "Anna", "Diaz", "23", "6", "2011", "Colombia"]
        passengersPage.YoungTeenData(dataTeen)

        dataKid = ["Femenino", "Maria", "Gomez", "21", "4", "2017", "Colombia"]
        passengersPage.KidData(dataKid)

        dataOwner = ["jose.aja00@gmail.com", "Colombia", "3194560279"]
        passengersPage.OwnerData(dataOwner)

        passengersPage.Confirm()
        
        servicesPage.SelectServices()
        DataSeatsGo =["17D","17E","17C"]
        seatsPage.chooseseats(DataSeatsGo)
        DataSeatsBack =["30A","30C","30B"]
        seatsPage.chooseseatsBack(DataSeatsBack)
        seatsPage.Confirm()
        paymentPage.pay()
        
     
