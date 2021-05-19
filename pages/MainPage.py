from .BasePage import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link_bug(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")

    def should_be_login_link(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")
