from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class HomePage(BasePage):
    PAGE_LOGO = (By.CSS_SELECTOR, "#hplogo")
    INPUT_TEXT = (By.CSS_SELECTOR, "#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
    MAKING_SENSE = (By.CSS_SELECTOR, "#rso > div:nth-child(1) > div > div > div.r > a > h3")

    def __init__(self, driver, page):
        super().__init__(driver)
        self.driver.get(page)

    def get_page_title(self, title):
        return self.get_title(title)

    def is_logo_displayed(self):
        return self.is_enabled(self.PAGE_LOGO)

    def get_text(self):
        return self.get_element_text(self.MAKING_SENSE)
