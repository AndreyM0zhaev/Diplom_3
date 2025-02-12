import pytest
import allure
from conftest import *
from data import *
from pages.main_page import MainPage


@allure.epic("Тесты для главной страницы")
@allure.feature("Главная страница")
class TestMainPage:
    @allure.story("Переход по кнопке 'Конструктор'")
    @allure.title('Проверка перехода по кнопке "Конструктор" на страницу оформления заказа')
    @allure.description('Тест проверяет, что появляется соответствующий текст со страницы оформления заказа')
    def test_click_constructor_button(self, browser):
        with allure.step("Инициализация главной страницы"):
            transition_button_constructor = MainPage(browser, BASE_URL)

        with allure.step("Проверка текста на странице оформления заказа"):
            assert transition_button_constructor.check_constructor_button() == BURGER

    @allure.story("Переход по кнопке 'Лента Заказов'")
    @allure.title('Проверка перехода по кнопке "Лента Заказов" на страницу ленты заказов')
    @allure.description('Тест проверяет, что появляется соответствующий текст со страницы ленты заказов')
    def test_check_orders_list_button(self, browser):
        with allure.step("Инициализация главной страницы"):
            transition_button_orders_list = MainPage(browser, BASE_URL)

        with allure.step("Проверка текста на странице ленты заказов"):
            assert transition_button_orders_list.check_orders_list_button() == FEED

    @allure.story("Детали ингредиента")
    @allure.title('Проверка появления всплывающего окна с деталями')
    @allure.description('Тест проверяет, что появляются детали ингредиента')
    def test_click_to_ingredient(self, browser):
        with allure.step("Инициализация главной страницы"):
            click_to_ingredient = MainPage(browser, BASE_URL)

        with allure.step("Проверка деталей ингредиента"):
            assert click_to_ingredient.click_to_ingredient() == DETAILS

    @allure.story("Закрытие деталей ингредиента")
    @allure.title('Проверка кнопки закрытия деталей ингредиента')
    @allure.description('Тест проверяет, что детали ингредиента закрываются и появляется соответствующий текст со страницы оформления заказа')
    def test_click_exit_icon(self, browser):
        with allure.step("Инициализация главной страницы"):
            click_to_icon_exit = MainPage(browser, BASE_URL)

        with allure.step("Проверка текста на странице оформления заказа"):
            assert click_to_icon_exit.click_exit_icon() == BURGER

    @allure.story("Счётчик ингредиента")
    @allure.title('Проверка, что при добавлении ингредиента в заказ, увеличивается счётчик данного ингредиента')
    @allure.description('Тест проверяет, что счётчик ингредиента увеличивается')
    def test_counter_ingredient_increase(self, browser):
        if browser.name == "firefox":
            return

        with allure.step("Инициализация главной страницы"):
            increases_counter_ingredient = MainPage(browser, BASE_URL)

        with allure.step("Проверка увеличения счётчика ингредиента"):
            assert increases_counter_ingredient.counter_ingredient_increase() == X2


    @allure.story("Оформление заказа")
    @allure.title('Проверка, что авторизованный пользователь может оформить заказ')
    @allure.description('Тест проверяет, что появляется сообщение об успешном оформлении заказа')
    @pytest.mark.usefixtures("login")
    def test_create_order_auth_user(self, browser):
        with allure.step("Инициализация главной страницы"):
            create_order_login_user = MainPage(browser, LOGIN_URL)

        with allure.step("Проверка сообщения об успешном оформлении заказа"):
            assert create_order_login_user.create_order_auth_user() == IN_PROGRESS
