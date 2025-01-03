import unittest
from pages.BookingOneWay import BookingOneWay
from selenium.webdriver.support import expected_conditions as EC
from pages.SelectFlyPage import SelectflyPage
from pages.PassengersPage import PassengersPage
from pages.Base import Base

class test_OneWay(unittest.TestCase):
    def setUp(self):
        self.base = Base(None)
        self.driver = self.base.desktop_connection()   
        self.driver.maximize_window()  
        self.base.go_to("https://nuxqa5.avtest.ink/")
        self.bookingOneWay = BookingOneWay(self.driver)
        self.selectFlyPage = SelectflyPage(self.driver)
        self.passengersPage = PassengersPage(self.driver)     
        

    def test_one(self):
        data = ["Ida"]
        self.bookingOneWay.search_fly(data)
        self.selectFlyPage.select_fly()
        dataAdult = ["Masculino","Jose","Maestre","20","10","1993","Colombia","No aplica"] 
        self.passengersPage.AdultData(dataAdult)
        dataBaby = ["Masculino","Juan","Maestre","15","12","2024","Colombia"]
        self.passengersPage.BabyData(dataBaby)

    #def tearDown(self):
        #if self.driver:
            #self.driver.quit()
            

if __name__ == "__main__":
    unittest.main()