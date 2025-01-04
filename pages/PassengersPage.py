from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Base import Base


class PassengersPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.AdultGender_Locator = "IdPaxGender_7E7E303030312D30312D30317E353334423438324433323244343535383534"
        self.AdultFirsName_Locator = (
            By.ID, "IdFirstName7E7E303030312D30312D30317E353334423438324433323244343535383534")
        self.AdultLastName_Locator = (
            By.ID, "IdLastName7E7E303030312D30312D30317E353334423438324433323244343535383534")
        self.AdultBirthDateDayLocator = "dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433323244343535383534_"
        self.AdultBirthDateMonthLocator = "dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433323244343535383534_"
        self.AdultBirthDateYearLocator = "dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433323244343535383534_"
        self.AdultnacionalityLocator = "IdDocNationality_7E7E303030312D30312D30317E353334423438324433323244343535383534"
        self.customerGramsLocator = "customerPrograms"

        self.BabyGender_Locator = "IdPaxGender_7E7E303030312D30312D30317E353334423438324433313244343535383534"
        self.BabyFirsName_Locator = (
            By.ID, "IdFirstName7E7E303030312D30312D30317E353334423438324433313244343535383534")
        self.BabyLastName_Locator = (
            By.ID, "IdLastName7E7E303030312D30312D30317E353334423438324433313244343535383534")
        self.BabyBirthDateDayLocator = "dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433313244343535383534_"
        self.BabyBirthDateMonthLocator = "dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433313244343535383534_"
        self.BabyBirthDateYearLocator = "dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433313244343535383534_"
        self.BabynacionalityLocator = "IdDocNationality_7E7E303030312D30312D30317E353334423438324433313244343535383534"

        self.TeenGender_Locator = "IdPaxGender_7E7E303030312D30312D30317E353334423438324433333244343535383534"
        self.TeenFirsName_Locator = (
            By.ID, "IdFirstName7E7E303030312D30312D30317E353334423438324433333244343535383534")
        self.TeenLastName_Locator = (
            By.ID, "IdLastName7E7E303030312D30312D30317E353334423438324433333244343535383534")
        self.TeenBirthDateDayLocator = "dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433333244343535383534_"
        self.TeenBirthDateMonthLocator = "dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433333244343535383534_"
        self.TeenBirthDateYearLocator = "dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433333244343535383534_"
        self.TeennacionalityLocator = "IdDocNationality_7E7E303030312D30312D30317E353334423438324433333244343535383534"

        self.KidGender_Locator = "IdPaxGender_7E7E303030312D30312D30317E353334423438324433343244343535383534"
        self.KidFirsName_Locator = (
            By.ID, "IdFirstName7E7E303030312D30312D30317E353334423438324433343244343535383534")
        self.KidLastName_Locator = (
            By.ID, "IdLastName7E7E303030312D30312D30317E353334423438324433343244343535383534")
        self.KidBirthDateDayLocator = "dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433343244343535383534_"
        self.KidBirthDateMonthLocator = "dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433343244343535383534_"
        self.KidBirthDateYearLocator = "dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433343244343535383534_"
        self.KidnacionalityLocator = "IdDocNationality_7E7E303030312D30312D30317E353334423438324433343244343535383534"

        self.email_Locator = (By.ID, "email")
        self.ComfirmEmail_Locator = (By.ID, "confirmEmail")
        self.PrefixPhone_locator = "phone_prefixPhoneId"
        self.Phone_locator = (By.ID, "phone_phoneNumberId")
        self.Terms_Locator = (By.ID, "sendNewsLetter")
        self.confirm_Locator = (
            By.CSS_SELECTOR, "button.page_button .button_label")

    def AdultData(self, data):

        if data[0] == "Masculino":
            wait = WebDriverWait(self.driver, 10)
            dropdown_button = wait.until(
                EC.element_to_be_clickable((By.ID, self.AdultGender_Locator)))
            dropdown_button.click()

            options = wait.until(EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, ".ui-dropdown_item")))
            for option in options:
                if option.text.strip() == "Masculino":
                    option.click()
                    break

        self.sender(data[1], self.AdultFirsName_Locator)
        self.sender(data[2], self.AdultLastName_Locator)

        self.click((By.ID, self.AdultBirthDateDayLocator))
        self.click((By.XPATH, "//span[text()='"+data[3]+"']"))
        self.click((By.ID, self.AdultBirthDateMonthLocator))
        self.click((By.XPATH, "//span[text()='"+data[4]+"']"))
        self.click((By.ID, self.AdultBirthDateYearLocator))
        self.click((By.XPATH, "//span[text()='"+data[5]+"']"))
        self.click((By.ID, self.AdultnacionalityLocator))
        self.click((By.XPATH, "//span[text()='"+data[6]+"']"))
        self.click((By.ID, self.customerGramsLocator))
        self.click((By.XPATH, "//span[text()='"+data[7]+"']"))

    def BabyData(self, DataBaBy):
        if DataBaBy[0] == "Masculino":
            wait = WebDriverWait(self.driver, 10)
            dropdown_button = wait.until(
                EC.element_to_be_clickable((By.ID, self.BabyGender_Locator)))
            dropdown_button.click()

            options = wait.until(EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, ".ui-dropdown_item")))
            for option in options:
                if option.text.strip() == "Masculino":
                    option.click()
                    break

            self.sender(DataBaBy[1], self.BabyFirsName_Locator)
            self.sender(DataBaBy[2], self.BabyLastName_Locator)

            self.click((By.ID, self.BabyBirthDateDayLocator))
            self.click((By.ID, self.BabyBirthDateDayLocator +
                       "-" + str(int(DataBaBy[3])-1)))
            self.click((By.ID, self.BabyBirthDateMonthLocator))
            self.click((By.ID, self.BabyBirthDateMonthLocator +
                       "-" + str(int(DataBaBy[4])-1)))
            self.click((By.ID, self.BabyBirthDateYearLocator))
            self.click((By.XPATH, "//span[text()='"+DataBaBy[5]+"']"))
            self.click((By.ID, self.BabynacionalityLocator))
            self.click((By.ID, self.BabynacionalityLocator+"-0"))

    def YoungTeenData(self, DataYoungTeen):
        if DataYoungTeen[0] == "Femenino":
            wait = WebDriverWait(self.driver, 10)
            dropdown_button = wait.until(
                EC.element_to_be_clickable((By.ID, self.TeenGender_Locator)))
            dropdown_button.click()

            options = wait.until(EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, ".ui-dropdown_item")))
            for option in options:
                if option.text.strip() == "Femenino":
                    option.click()
                    break
        self.sender(DataYoungTeen[1], self.TeenFirsName_Locator)
        self.sender(DataYoungTeen[2], self.TeenLastName_Locator)
        self.click((By.ID, self.TeenBirthDateDayLocator))
        self.click((By.ID, self.TeenBirthDateDayLocator +
                   "-" + str(int(DataYoungTeen[3])-1)))
        self.click((By.ID, self.TeenBirthDateMonthLocator))
        self.click((By.ID, self.TeenBirthDateMonthLocator +
                   "-" + str(int(DataYoungTeen[4])-1)))
        self.click((By.ID, self.TeenBirthDateYearLocator))
        self.click((By.XPATH, "//span[text()='"+DataYoungTeen[5]+"']"))
        self.click((By.ID, self.TeennacionalityLocator))
        self.click((By.ID, self.TeennacionalityLocator+"-0"))

    def KidData(self, DataKid):
        if DataKid[0] == "Femenino":
            wait = WebDriverWait(self.driver, 10)
            dropdown_button = wait.until(
                EC.element_to_be_clickable((By.ID, self.KidGender_Locator)))
            dropdown_button.click()

            options = wait.until(EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, ".ui-dropdown_item")))
            for option in options:
                if option.text.strip() == "Femenino":
                    option.click()
                    break
        self.sender(DataKid[1], self.KidFirsName_Locator)
        self.sender(DataKid[2], self.KidLastName_Locator)
        self.click((By.ID, self.KidBirthDateDayLocator))
        self.click((By.ID, self.KidBirthDateDayLocator +
                   "-" + str(int(DataKid[3])-1)))
        self.click((By.ID, self.KidBirthDateMonthLocator))
        self.click((By.ID, self.KidBirthDateMonthLocator +
                   "-" + str(int(DataKid[4])-1)))
        self.click((By.ID, self.KidBirthDateYearLocator))
        self.click((By.XPATH, "//span[text()='"+DataKid[5]+"']"))
        self.click((By.ID, self.KidnacionalityLocator))
        self.click((By.ID, self.KidnacionalityLocator+"-0"))

    def OwnerData(self, data):
        self.sender(data[0], self.email_Locator)
        self.sender(data[0], self.ComfirmEmail_Locator)
        self.click((By.ID, self.PrefixPhone_locator))
        self.click((By.ID, self.PrefixPhone_locator+"-0"))
        self.sender(data[2], self.Phone_locator)

    def Confirm(self):
        self.click(self.Terms_Locator)
        self.click(self.confirm_Locator)
