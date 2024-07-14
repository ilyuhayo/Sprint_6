from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not found {locator}')

    def find_elements_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f'Not found {locator}')

    def accept_cookies(self):
        self.find_element_located(BasePageLocators.ACCEPT_COOKIE_BUTTON).click()
