import allure
import pytest
from selenium.webdriver.common.by import By
from page_object.base_page import BasePage
from page_object.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from urls import URLS
from conftest import driver


class TestQuestionSection:
    def test_open_question_1(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(URLS.SCOOTER_SITE)
        main_page.accept_cookies()
        main_page.scroll_to_questions_list()
        main_page.wait_for_question(MainPageLocators.QUESTION_1)
        main_page.open_question(MainPageLocators.QUESTION_1)
        answer = main_page.get_answer(MainPageLocators.ANSWER_1)
        assert answer == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    def test_open_question_2(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(URLS.SCOOTER_SITE)
        main_page.accept_cookies()
        main_page.scroll_to_questions_list()
        main_page.wait_for_question(MainPageLocators.QUESTION_2)
        main_page.open_question(MainPageLocators.QUESTION_2)
        answer = main_page.get_answer(MainPageLocators.ANSWER_2)
        assert answer == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

    def test_open_question_3(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(URLS.SCOOTER_SITE)
        main_page.accept_cookies()
        main_page.scroll_to_questions_list()
        main_page.wait_for_question(MainPageLocators.QUESTION_3)
        main_page.open_question(MainPageLocators.QUESTION_3)
        answer = main_page.get_answer(MainPageLocators.ANSWER_3)
        assert answer == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    def test_open_question_4(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(URLS.SCOOTER_SITE)
        main_page.accept_cookies()
        main_page.scroll_to_questions_list()
        main_page.wait_for_question(MainPageLocators.QUESTION_4)
        main_page.open_question(MainPageLocators.QUESTION_4)
        answer = main_page.get_answer(MainPageLocators.ANSWER_4)
        assert answer == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    def test_open_question_5(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(URLS.SCOOTER_SITE)
        main_page.accept_cookies()
        main_page.scroll_to_questions_list()
        main_page.wait_for_question(MainPageLocators.QUESTION_5)
        main_page.open_question(MainPageLocators.QUESTION_5)
        answer = main_page.get_answer(MainPageLocators.ANSWER_5)
        assert answer == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

    def test_open_question_6(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(URLS.SCOOTER_SITE)
        main_page.accept_cookies()
        main_page.scroll_to_questions_list()
        main_page.wait_for_question(MainPageLocators.QUESTION_6)
        main_page.open_question(MainPageLocators.QUESTION_6)
        answer = main_page.get_answer(MainPageLocators.ANSWER_6)
        assert answer == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

    def test_open_question_7(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(URLS.SCOOTER_SITE)
        main_page.accept_cookies()
        main_page.scroll_to_questions_list()
        main_page.wait_for_question(MainPageLocators.QUESTION_7)
        main_page.open_question(MainPageLocators.QUESTION_7)
        answer = main_page.get_answer(MainPageLocators.ANSWER_7)
        assert answer == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    def test_open_question_8(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(URLS.SCOOTER_SITE)
        main_page.accept_cookies()
        main_page.scroll_to_questions_list()
        main_page.wait_for_question(MainPageLocators.QUESTION_8)
        main_page.open_question(MainPageLocators.QUESTION_8)
        answer = main_page.get_answer(MainPageLocators.ANSWER_8)
        assert answer == "Да, обязательно. Всем самокатов! И Москве, и Московской области."

