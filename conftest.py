import pytest
import allure
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from data import *
from pages.main_page import MainPage
from pages.login_page import LoginPage


from helpers.helpers_register_users import User


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

# Фикстура для логина конкретного пользователя
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

# Фикстура для создания пользователя через API
@pytest.fixture
def create_user():
    payload = User.registration_new_user()
    response = requests.post(BASE_URL + CREATE_USER, data=payload)
    yield payload, response
    token = response.json()["accessToken"]
    requests.delete(BASE_URL + DELETE_USER, headers={"Authorization": token})

# Фикстура для логина произвольного пользователя
@pytest.fixture
def login_random_user(browser, create_user):
    """
    Фикстура для логина в систему с помощью данных созданного пользователя.
    """
    create_user_data = create_user[0]  # Получение данных созданного пользователя
    main_page = MainPage(browser, BASE_URL)  # Инициализация страницы с заголовком
    main_page.click_user_account_button()  # Клик по кнопке "Личный кабинет"
    login_page = LoginPage(browser, LOGIN_URL)  # Инициализация страницы логина
    login_page.enter_user_data(create_user_data["email"], create_user_data["password"])  # Ввод данных для логина
    login_page.click_login_button()
    main_page = MainPage(browser, BASE_URL)  # Инициализация главной страницы
    main_page.wait_load_main_page()  # Ожидание загрузки главной страницы после логина

# Фикстура для создания заказа через API
@pytest.fixture
def create_order(create_user):
    """
    Фикстура для создания нового заказа через API и возврата его номера.
    """
    token = create_user[1].json()["accessToken"]  # Получение токена пользователя
    headers = {'Authorization': token}  # Заголовок с токеном для аутентификации
    response = requests.post(BASE_URL + CREATE_ORDER, headers=headers, data=valid_ingredients)  # Создание заказа через API
    return response.json()["order"]["number"]  # Возвращаем номер созданного заказа


