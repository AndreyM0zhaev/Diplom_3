import allure

from conftest import *
from data import *
from pages.user_account_page import UserAccountPage


@allure.epic("Тесты для личного кабинета пользователя")
@allure.feature("Личный кабинет")
@pytest.mark.usefixtures("login")
class TestUserAccount:

    @allure.title('Проверка перехода по клику на "Личный кабинет"')
    @allure.description('Тест проверяет, что переход по клику "Личный кабинет" осуществляется успешно')
    @allure.story("Переход в личный кабинет")
    def test_user_auth(self, browser):
        with allure.step("Инициализация страницы личного кабинета"):
            into_user_account = UserAccountPage(browser, LOGIN_URL)

        with allure.step("Переход в личный кабинет и получение текста профиля"):
            actual_result = into_user_account.check_user_account_button()

        with allure.step("Проверка, что текст профиля соответствует ожидаемому"):
            assert actual_result == PROFILE_TEXT, f"Ожидаемый текст: {PROFILE_TEXT}, Фактический текст: {actual_result}"

    @allure.title('Проверка перехода по клику на "История заказов"')
    @allure.description('Тест проверяет, что переход по клику "История заказов" осуществляется успешно')
    @allure.story("Переход в историю заказов")
    def test_click_history_orders_button(self, browser):
        with allure.step("Инициализация страницы личного кабинета"):
            click_history_orders = UserAccountPage(browser, LOGIN_URL)

        with allure.step("Переход в личный кабинет"):
            click_history_orders.check_user_account_button()

        with allure.step("Переход в историю заказов и получение названия заказа"):
            actual_result = click_history_orders.click_history_orders_button()

        with allure.step("Проверка, что название заказа соответствует ожидаемому"):
            assert actual_result == PRODUCT_TEXT, f"Ожидаемый текст: {PRODUCT_TEXT}, Фактический текст: {actual_result}"

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('Тест проверяет, что можно выйти из аккаунта')
    @allure.story("Выход из аккаунта")
    def test_logout(self, browser):
        with allure.step("Инициализация страницы личного кабинета"):
            logout = UserAccountPage(browser, LOGIN_URL)

        with allure.step("Переход в личный кабинет"):
            logout.check_user_account_button()

        with allure.step("Нажатие на кнопку 'Выйти' и получение текста кнопки 'Войти'"):
            actual_result = logout.click_logout_button()

        with allure.step("Проверка, что текст кнопки 'Войти' соответствует ожидаемому"):
            assert actual_result == LOG_IN_TEXT, f"Ожидаемый текст: {LOG_IN_TEXT}, Фактический текст: {actual_result}"