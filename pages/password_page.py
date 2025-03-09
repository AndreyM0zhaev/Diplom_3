from data import *
from pages.base_page import *
from locators.password_page_locators import PasswordPageLocators as PPL
from locators.login_page_locators import LoginPageLocator as LPL



class PasswordPage(BasePage):
    @allure.step('Нажатие на кнопку "Восстановить пароль"')
    def click_button_password_recovery(self):
        self.element_invisibility(LPL.SEARCH_ELEMENT)
        self.click(PPL.BUTTON_RECOVERY_PASSWORD)

    @allure.step('Возврат текста с кнопки "Восстановить"')
    def check_recovery_button(self):
        self.element_invisibility(LPL.SEARCH_ELEMENT)
        return self.get_text(PPL.BUTTON_RECOVERY)

    @allure.step('Заполнение поле email')
    def enter_email(self):
        self.add_text_into_element(PPL.INPUT_EMAIL, EMAIL)

    @allure.step('Нажатие на кнопку "Восстановить"')
    def click_recovery_button(self):
        self.element_invisibility(LPL.SEARCH_ELEMENT)
        self.click(PPL.BUTTON_RECOVERY)

    @allure.step('Возврат текста "Восстановление пароля"')
    def get_recovery_text(self):
        return self.get_text(PPL.TEXT_RECOVERY)

    @allure.step('Нажатие на переключатель показать/скрыть пароль')
    def click_switch(self):
        self.element_invisibility(LPL.SEARCH_ELEMENT)
        self.click(PPL.BUTTON_SWITCH)

    @allure.step('Проверка активности элемента')
    def check_element_visibility(self):
        self.element_invisibility(LPL.SEARCH_ELEMENT)
        return self.find_element(PPL.STATUS_ACTIVE)
