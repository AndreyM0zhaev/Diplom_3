import allure
from data import *
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.user_account_page import UserAccountPage


class TestFeedPage:


    @allure.title('Проверка открытия всплывающего окна с деталями')
    @allure.description('Тест проверяет, если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_details_in_history(self, browser, create_user, create_order, login_random_user):
        main_page = MainPage(browser, BASE_URL)
        order_page = FeedPage(browser, ORDERS_LIST_URL)
        main_page.check_orders_list_button()
        order_page.click_on_order_card()
        assert 'Флюоресцентный бургер' in order_page.get_feed_name_from_order_list()


    @allure.title('Проверка отображения существующего заказа из истории пользователя в ленте заказов')
    def test_display_orders_from_order_history_in_order_list(self, browser, create_user, login_random_user, create_order):

        create_order = MainPage(browser, BASE_URL)
        create_order.moving_ingredient()
        create_order.click_create_order_button()
        create_order.click_close_order_button()
        user_account = UserAccountPage(browser, BASE_URL)
        create_order.click_user_account_button()
        expected_result = user_account.click_history_orders_button_in_profile()
        orders_list = MainPage(browser, BASE_URL)
        orders_list.check_orders_list_button()
        display_orders = FeedPage(browser, ORDERS_LIST_URL)
        actual_result = display_orders.get_feed_name_from_order_list()
        assert expected_result == actual_result


    @allure.title('Проверка увеличения счетчика выполненных заказов за все время')
    @allure.description('Тест проверяет, что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_counter_increment_completed_for_all_time(self, browser, create_user, login_random_user):

        completed_for_all_time = FeedPage(browser, ORDERS_LIST_URL)
        expected_result = completed_for_all_time.get_orders_completed_all_time()
        create_order = MainPage(browser, BASE_URL)
        create_order.moving_ingredient()
        create_order.click_create_order_button()
        create_order.click_close_order_button()
        create_order.click_orders_list_button()
        actual_result = completed_for_all_time.get_orders_completed_all_time()
        assert expected_result < actual_result


    @allure.title('Проверка увеличения счетчика выполненных заказов за день')
    @allure.description('Тест проверяет, что при создании нового заказа счётчик Выполнено за день увеличивается')
    def test_counter_increase_completed_today(self, browser, create_user, login_random_user, create_order):

        completed_today = FeedPage(browser, ORDERS_LIST_URL)
        expected_result = completed_today.get_orders_completed_today()
        create_order = MainPage(browser, BASE_URL)
        create_order.moving_ingredient()
        create_order.click_create_order_button()
        create_order.click_close_order_button()
        create_order.click_orders_list_button()
        actual_result = completed_today.get_orders_completed_today()
        assert expected_result < actual_result



    @allure.title('Проверка появления номера созданного заказа в разделе "В работе"')
    @allure.description('Тест проверяет, что после оформления заказа его номер появляется в разделе В работе')
    def test_order_number_appeared_in_work(self, browser, create_user, login_random_user):

        create_order = MainPage(browser, BASE_URL)
        create_order.moving_ingredient()
        create_order.click_create_order_button()
        expected_result = create_order.get_number_order()
        create_order.click_close_order_button()
        create_order.click_orders_list_button()
        order_number_appeared = FeedPage(browser, ORDERS_LIST_URL)
        actual_result = order_number_appeared.get_number_in_progress()
        assert int(expected_result) == int(actual_result)



