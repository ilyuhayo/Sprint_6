from locators.order_page_locators import OrderPageLocators


class OrderTestData:
    CASE_1 = {
        "name": "Илья",
        "surname": "Золотов",
        "address": "Улица Пушкина, дом 123",
        "phone_number": "88005553535",
        "metro_station": "Черкизовская",
        "delivery_day": "029",
        "rental_period": "сутки",
        "scooter_color": OrderPageLocators.BLACK_PEARL_CHECKBOX,
        "comment": "Привезите как можно скорее"
    }

    CASE_2 = {
        "name": "Иван",
        "surname": "Петров",
        "address": "улица Мира, дом 321",
        "phone_number": "890123456789",
        "metro_station": "Сокольники",
        "delivery_day": "022",
        "rental_period": "двое суток",
        "scooter_color": OrderPageLocators.BLACK_PEARL_CHECKBOX,
        "comment": "Спасибо за оперативность"
    }
