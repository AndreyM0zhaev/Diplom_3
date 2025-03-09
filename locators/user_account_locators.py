from selenium.webdriver.common.by import By


class UserAccountLocators:
    # Локатор кнопки "Личный Кабинет"
    BUTTON_USER_ACCOUNT = [By.XPATH, "//p[text()='Личный Кабинет']/parent::a"]
    # Локатор текста "Профиль"
    TEXT_PROFILE = [By.XPATH, ".//a[text()='Профиль']"]
    # Локатор кнопки "История заказов"
    BUTTON_ORDERS_HISTORY = [By.XPATH, ".//a[text()='История заказов']"]
    # Локатор текста заказа "Флюоресцентный бургер"
    TEXT_ORDER = [By.XPATH, ".//h2[text()='Флюоресцентный бургер']"]
    # Локатор кнопки "Выход"
    BUTTON_EXIT = [By.XPATH, ".//button[text()='Выход']"]
