import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from pages.LanguagesPage import LanguagesPage
from pages.Base import Base



@pytest.fixture(scope="class")
def setup_and_teardown():
    base = Base(None)
    driver = base.desktop_connection()
    driver.maximize_window()
    base.go_to("https://nuxqa5.avtest.ink/")

    languagesPage = LanguagesPage(driver)

    Languages_Ob = {
        "Español": "avianca - encuentra tiquetes y vuelos baratos | Web oficial",
        "English": "avianca - Find cheap tickets and flights| Official site",
        "Français": "avianca - Trouvez des vols et billets pas chers | Site officiel",
        "Português": "avianca - encontrar passagens e voos baratos | Web Oficial"
    }

    yield languagesPage, Languages_Ob

    driver.quit()


@pytest.mark.usefixtures("setup_and_teardown")
class TestLanguages:
    def test_Language(self, setup_and_teardown):
        languagesPage, Languages_Ob = setup_and_teardown

        for language in Languages_Ob:
            languagesPage.SelectLanguages(language)
            assert languagesPage.VerifyLanguage() == Languages_Ob[language]
