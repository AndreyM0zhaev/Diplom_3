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


