import allure
import pytest
from selenium.webdriver.common.by import By
from page_object.base_page import BasePage
from page_object.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from locators.main_page_locators import AnswersText
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
        assert answer == AnswersText.ANSWER_TEXT_1

    def test_open_question_2(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(URLS.SCOOTER_SITE)
        main_page.accept_cookies()
        main_page.scroll_to_questions_list()
        main_page.wait_for_question(MainPageLocators.QUESTION_2)
        main_page.open_question(MainPageLocators.QUESTION_2)
        answer = main_page.get_answer(MainPageLocators.ANSWER_2)
        assert answer == AnswersText.ANSWER_TEXT_2

    def test_open_question_3(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(URLS.SCOOTER_SITE)
        main_page.accept_cookies()
        main_page.scroll_to_questions_list()
        main_page.wait_for_question(MainPageLocators.QUESTION_3)
        main_page.open_question(MainPageLocators.QUESTION_3)
        answer = main_page.get_answer(MainPageLocators.ANSWER_3)
        assert answer == AnswersText.ANSWER_TEXT_3

    def test_open_question_4(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(URLS.SCOOTER_SITE)
        main_page.accept_cookies()
        main_page.scroll_to_questions_list()
        main_page.wait_for_question(MainPageLocators.QUESTION_4)
        main_page.open_question(MainPageLocators.QUESTION_4)
        answer = main_page.get_answer(MainPageLocators.ANSWER_4)
        assert answer == AnswersText.ANSWER_TEXT_4

    def test_open_question_5(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(URLS.SCOOTER_SITE)
        main_page.accept_cookies()
        main_page.scroll_to_questions_list()
        main_page.wait_for_question(MainPageLocators.QUESTION_5)
        main_page.open_question(MainPageLocators.QUESTION_5)
        answer = main_page.get_answer(MainPageLocators.ANSWER_5)
        assert answer == AnswersText.ANSWER_TEXT_5

    def test_open_question_6(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(URLS.SCOOTER_SITE)
        main_page.accept_cookies()
        main_page.scroll_to_questions_list()
        main_page.wait_for_question(MainPageLocators.QUESTION_6)
        main_page.open_question(MainPageLocators.QUESTION_6)
        answer = main_page.get_answer(MainPageLocators.ANSWER_6)
        assert answer == AnswersText.ANSWER_TEXT_6

    def test_open_question_7(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(URLS.SCOOTER_SITE)
        main_page.accept_cookies()
        main_page.scroll_to_questions_list()
        main_page.wait_for_question(MainPageLocators.QUESTION_7)
        main_page.open_question(MainPageLocators.QUESTION_7)
        answer = main_page.get_answer(MainPageLocators.ANSWER_7)
        assert answer == AnswersText.ANSWER_TEXT_7

    def test_open_question_8(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(URLS.SCOOTER_SITE)
        main_page.accept_cookies()
        main_page.scroll_to_questions_list()
        main_page.wait_for_question(MainPageLocators.QUESTION_8)
        main_page.open_question(MainPageLocators.QUESTION_8)
        answer = main_page.get_answer(MainPageLocators.ANSWER_8)
        assert answer == AnswersText.ANSWER_TEXT_8

