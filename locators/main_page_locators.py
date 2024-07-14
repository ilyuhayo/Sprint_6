from selenium.webdriver.common.by import By



class MainPageLocators:

    QUESTIONS_LIST = (By.CLASS_NAME, "Home_FAQ__3uVm4")
    QUESTION_1 = (By.XPATH, "//div[@id='accordion__heading-0']")
    ANSWER_1 = (By.XPATH, "//p[contains(text(), 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')]")
    QUESTION_2 = (By.XPATH, "//div[@id='accordion__heading-1']")
    ANSWER_2 = (By.XPATH, "//p[contains(text(), 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')]")
    QUESTION_3 = (By.XPATH, "//div[@id='accordion__heading-2']")
    ANSWER_3 = (By.XPATH, "//p[contains(text(), 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')]")
    QUESTION_4 = (By.XPATH, "//div[@id='accordion__heading-3']")
    ANSWER_4 = (By.XPATH, "//p[contains(text(), 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.')]")
    QUESTION_5 = (By.XPATH, "//div[@id='accordion__heading-4']")
    ANSWER_5 = (By.XPATH, "//p[contains(text(), 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.')]")
    QUESTION_6 = (By.XPATH, "//div[@id='accordion__heading-5']")
    ANSWER_6 = (By.XPATH, "//p[contains(text(), 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')]")
    QUESTION_7 = (By.XPATH, "//div[@id='accordion__heading-6']")
    ANSWER_7 = (By.XPATH, "//p[contains(text(), 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.')]")
    QUESTION_8 = (By.XPATH, "//div[@id='accordion__heading-7']")
    ANSWER_8 = (By.XPATH, "//p[contains(text(), 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')]")

    ORDER_BUTTON_HEADER = (By.XPATH, "//button[@class='Button_Button__ra12g']")
