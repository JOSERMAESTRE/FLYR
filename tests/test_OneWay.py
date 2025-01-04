import unittest
from pages.BookingOneWay import BookingOneWay
from selenium.webdriver.support import expected_conditions as EC
from pages.SelectFlyPage import SelectflyPage
from pages.PassengersPage import PassengersPage
from pages.Base import Base
from pages.ServicesPage import ServicesPage
from pages.SeatsPage import SeatsPage
from pages.PaymentPage import PaymentPage
from pages.ComfirmationPage import ComfirmationPage
import time
class test_OneWay(unittest.TestCase):
    def setUp(self):
        self.base = Base(None)
        self.driver = self.base.desktop_connection()   
        self.driver.maximize_window()  
        self.base.go_to("https://nuxqa5.avtest.ink/")
        self.bookingOneWay = BookingOneWay(self.driver)
        self.selectFlyPage = SelectflyPage(self.driver)
        self.passengersPage = PassengersPage(self.driver)
        self.servicesPage = ServicesPage(self.driver)
        self.seatsPage = SeatsPage(self.driver)
        self.paymentPage = PaymentPage(self.driver)
        self.comfirmationPage = ComfirmationPage(self.driver)
        

    def test_one(self):
        data = ["Ida"]
        self.bookingOneWay.search_fly(data)
        self.selectFlyPage.select_fly()
        dataAdult = ["Masculino","Jose","Maestre","20","10","1993","Colombia","No aplica"] 
        self.passengersPage.AdultData(dataAdult)
        dataBaby = ["Masculino","Juan","Maestre","15","12","2024","Colombia"]
        self.passengersPage.BabyData(dataBaby)
        dataTeen = ["Femenino","Anna","Diaz","23","6","2011","Colombia"]
        self.passengersPage.YoungTeenData(dataTeen)
        dataKid = ["Femenino","Maria","Gomez","21","4","2017","Colombia"]
        self.passengersPage.KidData(dataKid)
        dataOwner = ["jose.rafan00@gmail.com","Colombia","3194560279"]
        self.passengersPage.OwnerData(dataOwner)
        self.passengersPage.Confirm()
        self.servicesPage.Confirm()
        self.seatsPage.chooseseats()
        self.seatsPage.Confirm()
        self.paymentPage.pay()
        assert self.comfirmationPage.Confirmation() == "¡Tu reserva está confirmada!"
        time.sleep(120)
    def tearDown(self):
        if self.driver:
           pass
            
if __name__ == "__main__":
     try:
        unittest.main()
     except Exception as e:
        print(f"Error capturado: {e}")
        input("Presiona Enter para cerrar el navegador manualmente...")