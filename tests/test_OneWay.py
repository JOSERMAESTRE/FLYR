import allure
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from pages.ComfirmationPage import ComfirmationPage
from pages.PaymentPage import PaymentPage
from pages.SeatsPage import SeatsPage
from pages.ServicesPage import ServicesPage
from pages.Base import Base
from pages.PassengersPage import PassengersPage
from pages.SelectFlyPage import SelectflyPage
from selenium.webdriver.support import expected_conditions as EC
from pages.BookingOneWay import BookingOneWay

# Definir el fixture para configurar y cerrar el WebDriver


@pytest.fixture(scope="function")
def setup_and_teardown():
    base = Base(None)
    driver = base.desktop_connection()
    driver.maximize_window()
    base.go_to("https://nuxqa5.avtest.ink/")

    bookingOneWay = BookingOneWay(driver)
    selectFlyPage = SelectflyPage(driver)
    passengersPage = PassengersPage(driver)
    servicesPage = ServicesPage(driver)
    seatsPage = SeatsPage(driver)
    paymentPage = PaymentPage(driver)
    comfirmationPage = ComfirmationPage(driver)

    yield bookingOneWay, selectFlyPage, passengersPage, servicesPage, seatsPage, paymentPage, comfirmationPage, driver

    # Cerrar el WebDriver después de la prueba
    driver.quit()

# Test para la reserva de un vuelo de ida

@allure.feature("One Way Trip")
@allure.title("Validación de One Way Trip")
@pytest.mark.usefixtures("setup_and_teardown")
class TestOneWay:
    def test_one(self, setup_and_teardown):
        bookingOneWay, selectFlyPage, passengersPage, servicesPage, seatsPage, paymentPage, comfirmationPage, driver = setup_and_teardown

        data = ["Ida"]
        bookingOneWay.search_fly(data)
        selectFlyPage.select_fly()
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

        dataOwner = ["jose.n00@gmail.com", "Colombia", "3194560279"]
        passengersPage.OwnerData(dataOwner)

        passengersPage.Confirm()
        servicesPage.Confirm()
        DataSeats = ["16A","16B","16C"]
        seatsPage.chooseseats(DataSeats)
        seatsPage.Confirm()
        paymentPage.pay()
        assert comfirmationPage.Confirmation() == "¡Tu vuelo a Bogotá se encuentra en espera!"
        
