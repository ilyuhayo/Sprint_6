from locators.order_page_locators import OrderPageLocators


class OrderTestData:
    CASE_1 = {
        "name": "Илья",
        "surname": "Золотов",
        "address": "Улица Пушкина, дом 123",
        "phone_number": "88005553535",
        "scooter_color": OrderPageLocators.BLACK_PEARL_CHECKBOX,
        "comment": "Привезите как можно скорее"
    }

    CASE_2 = {
        "name": "Иван",
        "surname": "Петров",
        "address": "улица Мира, дом 321",
        "phone_number": "890123456789",
        "scooter_color": OrderPageLocators.GRAY_HOPELESSNESS,
        "comment": "Спасибо за оперативность"
    }
