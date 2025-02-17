from selenium.webdriver.common.by import By

class PasswordPageLocators:
    """
    Локаторы для тестов восстановления пароля.
    """
    BUTTON_RECOVERY_PASSWORD = [By.XPATH, ".//a[text()='Восстановить пароль']"]  # Кнопка "Восстановить пароль"
    INPUT_EMAIL = [By.XPATH, ".//input[@type='text']"]  # Поле ввода email
    BUTTON_RECOVERY = [By.XPATH, ".//button[text()='Восстановить']"]  # Кнопка "Восстановить"
    BUTTON_SWITCH = [By.XPATH, ".//div[contains(@class, 'input__icon')]"]  # Кнопка переключения видимости пароля
    TEXT_RECOVERY = [By.XPATH, ".//h2[text()='Восстановление пароля']"]  # Заголовок "Восстановление пароля"
    STATUS_ACTIVE = [By.XPATH, ".//div[contains(@class, 'input_status_active')]"]  # Статус активного поля ввода