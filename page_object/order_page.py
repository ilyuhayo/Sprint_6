from page_object.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):
    def set_name(self, name):
        self.find_element_located(OrderPageLocators.NAME_FIELD).send_keys(name)

    def set_surname(self, surname):
        self.find_element_located(OrderPageLocators.SURNAME_FIELD).send_keys(surname)

    def set_address(self, address):
        self.find_element_located(OrderPageLocators.ADDRESS_FIELD).send_keys(address)

    def select_metro_station(self):
        self.find_element_located(OrderPageLocators.METRO_STATION_SELECTOR).click()

    def set_phone_number(self, number):
        self.find_element_located(OrderPageLocators.PHONE_NUMBER_FIELD).send_keys(number)

    def click_next_button(self):
        self.find_element_located(OrderPageLocators.NEXT_BUTTON).click()

    def select_delivery_day(self):
        self.find_element_located(OrderPageLocators.DELIVERY_SCOOTER_DAY_FIELD).click()

    def select_rental_period(self):
        self.find_element_located(OrderPageLocators.RENTAL_PERIOD_FIELD).click()

    def select_scooter_color(self, locator):
        self.find_element_located(locator).click()
    def leave_a_comment_for_courier(self, comment):
        self.find_element_located(OrderPageLocators.COURIER_COMMENTS_FIELD).send_keys(comment)

    def click_order_button(self):
        self.find_element_located(OrderPageLocators.ORDER_BUTTON).click()

    def confirm_order(self):
        self.find_element_located(OrderPageLocators.CONFIRM_ORDER_BUTTON).click()

    def get_order_success_message(self):
        return self.find_element_located(OrderPageLocators.CREATED_ORDER_WINDOW).text

    def click_logo_scooter(self):
        self.find_element_located(OrderPageLocators.SCOOTER_LOGO).click()

    def click_check_status_button(self):
        self.find_element_located(OrderPageLocators.GET_STATUS_BUTTON).click()

    def click_logo_yandex(self):
        self.find_element_located(OrderPageLocators.YANDEX_LOGO).click()






