import pytest
import allure

from data import *
from conftest import *
from pages.password_page import PasswordPage



class TestPasswordRecovery:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    @allure.description('Тест проверяет, что работает переход на страницу восстановления пароля по '
                        'кнопке "Восстановить пароль"')
    def test_button_password_recovery(self, browser):
        password_recovery = PasswordPage(browser, LOGIN_URL)
        password_recovery.click_button_password_recovery()
        actual_result = password_recovery.check_recovery_button()
        assert actual_result == RECOVERY_TEXT

    @allure.title('Проверка ввода почты и клика по кнопке "Восстановить"')
    @allure.description('Тест проверяет, что можно ввести почту и нажать кнопку "Восстановить"')
    def test_email_and_recovery_button(self, browser):
        recovery_button = PasswordPage(browser, PASSWORD_RECOVERY_URL)
        recovery_button.enter_email()
        recovery_button.click_recovery_button()
        actual_result = recovery_button.get_recovery_text()
        assert actual_result == PASSWORD_RECOVERY_TEXT

    @allure.title('Проверка активности поля "Пароль" после нажатия кнопки показать/скрыть')
    @allure.description('Тест проверяет, что клик по кнопке показать/скрыть пароль делает поле '
                        'активным — подсвечивает его')
    def test_click_switch(self, browser):
        button_show_hide = PasswordPage(browser, PASSWORD_RECOVERY_URL)
        button_show_hide.enter_email()
        button_show_hide.click_recovery_button()
        button_show_hide.click_switch()
        assert button_show_hide.check_element_visibility() is not None

