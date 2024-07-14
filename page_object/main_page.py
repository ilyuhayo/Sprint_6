from page_object.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def scroll_to_questions_list(self):
        question_list = self.find_element_located(MainPageLocators.QUESTIONS_LIST)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question_list)

    def wait_for_question(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def open_question(self, locator):
        self.find_element_located(locator).click()

    def get_answer(self, locator):
        return self.find_element_located(locator).text

    def click_order_button(self, locator):
        self.find_element_located(locator).click()









