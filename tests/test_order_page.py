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
from conftest import driver


class TestOrderPage:
    def test_fill_order_form_case_1(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        main_page.accept_cookies()
        main_page.click_order_button(MainPageLocators.ORDER_BUTTON_HEADER)
        order_page = OrderPage(driver)
        order_page.set_name("Илья")
        order_page.set_surname("Золотов")
        order_page.set_address("Улица Пушкина, дом 123")
        order_page.select_metro_station()
        order_page.find_element_located((By.XPATH, "//div[text()='Черкизовская']")).click()
        order_page.set_phone_number("88005553535")
        order_page.click_next_button()
        order_page.select_delivery_day()
        order_page.find_element_located((By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--029']")).click()
        order_page.select_rental_period()
        order_page.find_element_located((By.XPATH, "//div[text()='сутки']")).click()
        order_page.select_scooter_color(OrderPageLocators.BLACK_PEARL_CHECKBOX)
        order_page.leave_a_comment_for_courier("Привезите как можно скорее")
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

    @pytest.mark.parametrize(
        "name, surname, address, phone_number, metro_station, delivery_day, rental_period, scooter_color, comment",
        [("Иван", "Петров", "улица Мира, дом 321", "890123456789", "Сокольники", "022", "двое суток",
          OrderPageLocators.BLACK_PEARL_CHECKBOX, "Спасибо за оперативность")])
    def test_fill_order_form_case_2(self, driver, name, surname, address, phone_number, metro_station, delivery_day,
                                    rental_period, scooter_color, comment):
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        main_page.accept_cookies()
        main_page.click_order_button(MainPageLocators.ORDER_BUTTON_HEADER)
        order_page = OrderPage(driver)
        order_page.set_name(name)
        order_page.set_surname(surname)
        order_page.set_address(address)
        order_page.select_metro_station()
        order_page.find_element_located((By.XPATH, f"//div[text()='{metro_station}']")).click()
        order_page.set_phone_number(phone_number)
        order_page.click_next_button()
        order_page.select_delivery_day()
        order_page.find_element_located(
            (By.XPATH, f"//div[@class='react-datepicker__day react-datepicker__day--{delivery_day}']")).click()
        order_page.select_rental_period()
        order_page.find_element_located((By.XPATH, f"//div[text()='{rental_period}']")).click()
        order_page.select_scooter_color(scooter_color)
        order_page.leave_a_comment_for_courier(comment)
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
