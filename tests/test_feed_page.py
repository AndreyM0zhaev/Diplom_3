import time

from pages.base_page import BasePage
import pytest
import allure

from data import *
from conftest import *
from locators.feed_page_locators import FeedPageLocators as FPL
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.user_account_page import UserAccountPage
from helpers.helpers_requests import Order


class TestFeedPage:


    @allure.title('Проверка открытия всплывающего окна с деталями')
    @allure.description('Тест проверяет, если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_get_order_details(self, browser):
        order_details = FeedPage(browser, ORDERS_LIST_URL)
        assert order_details.get_order_details() == COMPOSITION

    @allure.title('Проверка, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_orders_in_history(self, browser, create_user, create_order, login_random_user):
        order_page = Order()
        main_page = MainPage(browser, BASE_URL)
        details_page = FeedPage(browser, ORDERS_LIST_URL)
        main_page.check_orders_list_button()
        details_page.click_on_order_card()
        time.sleep(5)
        assert 'Флюоресцентный бургер' in details_page.get_feed_name_from_order_list()

        # # page.click_feed_btn()  # Переход в "Лента заказов"
        # user_order = str(order_page.get_user_orders(create_user))  # Получение заказа пользователя
        # orders_history_in_feed = details_page.get_orders_history()  # Получение истории заказов на странице "Лента заказов"
        # assert user_order in orders_history_in_feed  # Проверка отображения заказа в "Лента заказов"
