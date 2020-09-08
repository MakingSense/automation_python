from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # Basic method to click on an element
    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    # Basic method to enter keys into a input field
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # Basic method to get the text from an element
    def get_element_text(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text

    # Basic method to verify if an element is already enabled in the DOM
    def is_enabled(self, by_locator):
        return bool(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)))

    # Basic method to get the page's title
    def get_title(self, title):
        return WebDriverWait(self.driver, 10).until(EC.title_is(title))
