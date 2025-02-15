import allure

from locators.user_account_locators import UserAccountLocators as UAL
from locators.login_page_locators import LoginPageLocator as LPL
from pages.base_page import *
from locators.main_page_locators import MainPageLocator as MPL


@allure.epic("Тесты для личного кабинета пользователя")
@allure.feature("Личный кабинет")
class UserAccountPage(BasePage):
    @allure.step('Нажатие на кнопку "Личный кабинет"')
    def click_user_account_button(self):
        self.element_invisibility(LPL.SEARCH_ELEMENT)
        self.click(UAL.BUTTON_USER_ACCOUNT)

    @allure.step('Переход в личный кабинет и возврат текста со страницы')
    def check_user_account_button(self):
        self.element_invisibility(LPL.SEARCH_ELEMENT)
        self.click(UAL.BUTTON_USER_ACCOUNT)
        self.element_invisibility(LPL.SEARCH_ELEMENT)
        return self.get_text(UAL.TEXT_PROFILE)

    @allure.step('Переход в историю заказов и возврат названия заказа')
    def click_history_orders_button(self):
        self.click(UAL.BUTTON_ORDERS_HISTORY)
        return self.get_text(UAL.TEXT_ORDER)

    @allure.step('Нажатие кнопки "Выйти"')
    def click_logout_button(self):
        self.click(UAL.BUTTON_EXIT)
        self.element_invisibility(LPL.SEARCH_ELEMENT)
        return self.get_text(LPL.BUTTON_LOGIN)

