import allure
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from pages.LanguagesPage import LanguagesPage
from pages.FooterPage import FooterPage
from pages.Base import Base



@pytest.fixture(scope="function")
def setup_and_teardown():
    base = Base(None)
    driver = base.desktop_connection()
    driver.maximize_window()
    base.go_to("https://nuxqa5.avtest.ink/")

    footerpage = FooterPage(driver)
    languagesPage = LanguagesPage(driver)

    options = {
        "English": ["Accessibility", "avianca - Accessibility plan"],
        "Español": ["Vuelos baratos", "avianca - Promociones y ofertas de vuelos"],
        "Português": ["aviancadirect", "avianca - NDC – Avianca Direct"],
        "Français": ["Nous sommes avianca", "avianca - Nous sommes avianca"],
    }

    yield footerpage, languagesPage, options

    driver.quit()

@allure.feature("Testing Footers links")
@allure.title("Validación de navegacion Footer")
@pytest.mark.usefixtures("setup_and_teardown")
class TestFooter:
    def test_Footer(self, setup_and_teardown):
        footerpage, languagesPage, options = setup_and_teardown

        for language, titles in options.items():
            languagesPage.SelectLanguages(language)

            footerpage.GoFooterPage(titles[0])

            assert footerpage.VerifyFooter().strip() == titles[1].strip()
