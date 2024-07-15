from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_SELECTOR = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_NUMBER_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    DELIVERY_SCOOTER_DAY_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_FIELD = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    BLACK_PEARL_CHECKBOX = (By.XPATH, "//input[@id='black']")
    GRAY_HOPELESSNESS = (By.XPATH, "//input[@id='grey']")
    COURIER_COMMENTS_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    CREATED_ORDER_WINDOW = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    GET_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    CHERKIZOVSKAYA_METRO_STATION = (By.XPATH, "//div[text()='Черкизовская']")
    JULY_DATE_29 = (By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--029']")
    RENT_DAYS_2 = (By.XPATH, "//div[text()='двое суток']")
    SOKOLNIKI_METRO_STATION = (By.XPATH, "//div[text()='Сокольники']")
    JULY_DATE_22 = (By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--022']")
    RENT_DAYS_3 = (By.XPATH, "//div[text()='трое суток']")


