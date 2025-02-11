import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from data import BASE_URL, LOGIN_URL
from pages.login_page import LoginPage


@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    """
    Фикстура для инициализации и завершения работы веб-драйвера.
    Поддерживает запуск тестов на Chrome и Firefox.
    Возвращает экземпляр драйвера для использования в тестах.
    """
    browser = None

    with allure.step(f"Инициализация браузера: {request.param}"):
        if request.param == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            browser = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )
        elif request.param == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--start-maximized")
            browser = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )

    with allure.step(f"Открытие URL: {BASE_URL}"):
        browser.get(BASE_URL)

    yield browser

    with allure.step("Завершение работы браузера"):
        browser.quit()


@pytest.fixture()
def login(browser):
    """
    Фикстура для авторизации пользователя.
    Выполняет вход в систему с использованием данных из data.py.
    """
    with allure.step("Инициализация страницы логина"):
        login_user = LoginPage(browser, LOGIN_URL)

    with allure.step("Ввод email"):
        login_user.input_email()

    with allure.step("Ввод пароля"):
        login_user.input_password()

    with allure.step("Нажатие кнопки 'Войти'"):
        login_user.click_login_button()