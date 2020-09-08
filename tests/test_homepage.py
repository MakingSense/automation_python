from pytest import mark
from selenium.webdriver.common.keys import Keys
from tests.test_base import BaseTests
from pages.HomePage import HomePage


@mark.smoke
class HomePageTests(BaseTests):

    page_title = "software"

    @mark.ui
    def test_ui_navigate_to_makingsense_page(self):
        self.HomePage = HomePage(self.driver, 'https://www.google.com')
        assert self.HomePage.is_logo_displayed()

    def test_ui_enter_text(self):
        self.HomePage = HomePage(self.driver, 'https://www.google.com')
        self.HomePage.do_send_keys(self.HomePage.INPUT_TEXT, "making sense")
        self.HomePage.do_send_keys(self.HomePage.INPUT_TEXT, Keys.ENTER)
        assert self.HomePage.get_text() == "Making Sense"

