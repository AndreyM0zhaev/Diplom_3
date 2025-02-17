from data import *
from pages.base_page import *
from locators.login_page_locators import *
from locators.main_page_locators import *
from locators.login_page_locators import LoginPageLocator as LPL


class LoginPage(BasePage):

    @allure.step('Вводим email и пароль')
    def enter_user_data(self, email, password):
        self.wait_for_load_element(LPL.INPUT_EMAIL)
        self.click_on_element(LPL.INPUT_EMAIL)
        self.add_text_into_element(LPL.INPUT_EMAIL, email)
        self.click_on_element(LPL.INPUT_PASSWORD)
        self.add_text_into_element(LPL.INPUT_PASSWORD, password)

    @allure.step('Заполнение поля email')
    def input_email(self):
        self.add_text_into_element(LoginPageLocator.INPUT_EMAIL, EMAIL)

    @allure.step('Заполнение поля пароль')
    def input_password(self):
        self.add_text_into_element(LoginPageLocator.INPUT_PASSWORD, PASSWORD)

    @allure.step('Возврат текста со страницы создания заказа после перехода по кнопке "Войти"')
    def click_login_button(self):
        self.element_invisibility(LoginPageLocator.SEARCH_ELEMENT)
        self.click(LoginPageLocator.BUTTON_LOGIN)
        self.find_element(MainPageLocator.TEXT_BURGER)
