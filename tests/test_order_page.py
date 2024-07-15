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
from conftest import driver


class TestOrderPage:
    def test_fill_order_form_case_1(self, driver):
        data = OrderTestData.CASE_1
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
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
        order_success_message = order_page.shows_created_order_window()
        expected_success_message = "Заказ оформлен"
        assert expected_success_message in order_success_message
        order_page.click_check_status_button()
        order_page.click_logo_scooter()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"
        order_page.click_logo_yandex()
        windows_handles = driver.window_handles
        driver.switch_to.window(windows_handles[-1])
        expected_url = "https://dzen.ru/?yredirect=true"
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_to_be(expected_url))
        assert expected_url in driver.current_url


    def test_fill_order_form_case_2(self, driver):
        data = OrderTestData.CASE_2
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        main_page.accept_cookies()
        main_page.click_order_button(MainPageLocators.ORDER_BUTTON_HEADER)
        order_page = OrderPage(driver)
        order_page.set_name(data["name"])
        order_page.set_surname(data["surname"])
        order_page.set_address(data["address"])
        order_page.select_metro_station()
        order_page.find_element_located(OrderPageLocators.SOKOLNIKI_METRO_STATION).click()
        order_page.set_phone_number(data["phone_number"])
        order_page.click_next_button()
        order_page.select_delivery_day()
        order_page.find_element_located(OrderPageLocators.JULY_DATE_22).click()
        order_page.select_rental_period()
        order_page.find_element_located(OrderPageLocators.RENT_DAYS_3).click()
        order_page.select_scooter_color(data["scooter_color"])
        order_page.leave_a_comment_for_courier(data["comment"])
        order_page.click_order_button()
        order_page.confirm_order()
        order_success_message = order_page.shows_created_order_window()
        expected_success_message = "Заказ оформлен"
        assert expected_success_message in order_success_message
        order_page.click_check_status_button()
        order_page.click_logo_scooter()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"
        order_page.click_logo_yandex()
        windows_handles = driver.window_handles
        driver.switch_to.window(windows_handles[-1])
        expected_url = "https://dzen.ru/?yredirect=true"
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_to_be(expected_url))
        assert expected_url in driver.current_url
