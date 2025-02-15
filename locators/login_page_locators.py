from selenium.webdriver.common.by import By


class LoginPageLocator:
    # Локаторы для полей ввода и кнопок на странице входа
    INPUT_EMAIL = [By.XPATH, ".//*[text()='Email']/following-sibling::input"]  # Поле ввода Email
    INPUT_PASSWORD = [By.XPATH, ".//*[text()='Пароль']/following-sibling::input"]  # Поле ввода пароля
    BUTTON_LOGIN = [By.XPATH, ".//button[text()='Войти']"]  # Кнопка "Войти"

    # Локатор для поиска элемента, указывающего на загрузку или модальное окно
    SEARCH_ELEMENT = [By.XPATH, ".//*[contains(@class, 'Modal_modal__loading')]/following::div[@class='Modal_modal_overlay__x2ZCr']"]  # Элемент, указывающий на загрузку
