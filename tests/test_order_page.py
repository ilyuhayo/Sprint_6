import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.base_page import BasePage
from page_object.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from page_object.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from test_constants import OrderTestData
from urls import URLS
from conftest import driver


class TestOrderPage:
    @pytest.mark.parametrize("test_input", [(OrderTestData.CASE_1), (OrderTestData.CASE_2)])
    def test_fill_order_form(self, test_input, driver):
        data = test_input
        main_page = MainPage(driver)
        main_page.go_to_site(URLS.SCOOTER_SITE)
        main_page.accept_cookies()
        main_page.click_order_button(MainPageLocators.ORDER_BUTTON_HEADER)
        order_page = OrderPage(driver)
        order_page.set_name(data["name"])
        order_page.set_surname(data["surname"])
        order_page.set_address(data["address"])
        order_page.select_metro_station()
        order_page.find_element_located(OrderPageLocators.CHERKIZOVSKAYA_METRO_STATION).click()
        order_page.set_phone_number(data["phone_number"])
        order_page.click_next_button()
        order_page.select_delivery_day()
        order_page.find_element_located(OrderPageLocators.JULY_DATE_29).click()
        order_page.select_rental_period()
        order_page.find_element_located(OrderPageLocators.RENT_DAYS_2).click()
        order_page.select_scooter_color(data["scooter_color"])
        order_page.leave_a_comment_for_courier(data["comment"])
        order_page.click_order_button()
        order_page.confirm_order()
        order_success_message = order_page.get_order_success_message()
        assert "Заказ оформлен" in order_success_message

    def test_check_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(URLS.SCOOTER_SITE)
        main_page.accept_cookies()
        main_page.click_order_button(MainPageLocators.ORDER_BUTTON_HEADER)
        order_page = OrderPage(driver)
        order_page.click_logo_scooter()
        base_page = BasePage(driver)
        assert base_page.get_current_url() == URLS.SCOOTER_SITE


    def test_check_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(URLS.SCOOTER_SITE)
        main_page.accept_cookies()
        main_page.click_order_button(MainPageLocators.ORDER_BUTTON_HEADER)
        order_page = OrderPage(driver)
        order_page.click_logo_yandex()
        base_page = BasePage(driver)
        windows_handles = base_page.get_window_handles()
        base_page.get_switch_to_window(windows_handles[-1])
        expected_url = URLS.YANDEX_SITE
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_to_be(expected_url))
        base_page = BasePage(driver)
        assert expected_url in base_page.get_current_url()

