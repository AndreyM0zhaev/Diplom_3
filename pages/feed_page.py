from pages.base_page import *
from data import *
from locators.feed_page_locators import FeedPageLocators as FPL
from locators.login_page_locators import LoginPageLocator as LPL



class FeedPage(BasePage):
    @allure.step('Нажатие на заказ и получение текста с деталями заказа')
    def get_order_details(self):
        self.element_invisibility(LPL.SEARCH_ELEMENT)
        self.click(FPL.BUTTON_ORDER)
        return self.get_text(FPL.COMPOUND)

    @allure.step('Открываем Ленту заказов')
    def open_feed_page(self):
        self.open_page(ORDERS_LIST_URL)
        self.wait_for_load_element(FPL.COMPLETED_TODAY)

    @allure.step('Получаем список элементов страницы со счетчиками "Выполнено за всё время" и "Выполнено за сегодня"')
    def get_list_orders_completed_all_time(self):
        # self.element_invisibility(LPL.SEARCH_ELEMENT)
        # return self.get_text(FPL.COMPLETED_ALL_TIME)
        elements = self.wait_for_load_all_elements(FPL.COMPLETED_ALL_TIME)
        return elements

    @allure.step('Получение количества заказов за все время')
    def get_orders_completed_all_time(self):
        # self.element_invisibility(LPL.SEARCH_ELEMENT)
        # return self.get_text(FPL.COMPLETED_ALL_TIME)
        elements = self.get_list_orders_completed_all_time()
        return int(str(elements[0].text))

    @allure.step('Получение количества заказов за сегодня')
    def get_orders_completed_today(self):
        # return self.get_text(FPL.COMPLETED_TODAY)
        elements = self.get_list_orders_completed_all_time()
        return int(str(elements[1].text))




    @allure.step('Получение номера заказа "В процессе"')
    def get_number_in_progress(self):
        self.element_invisibility(LPL.SEARCH_ELEMENT)
        return self.get_text(FPL.IN_PROGRESS)

    @allure.step('Получение названия заказа из Ленты Заказов')
    def get_feed_name_from_order_list(self):
        self.element_invisibility(LPL.SEARCH_ELEMENT)
        return self.get_text(FPL.FEED_NAME)

    @allure.step('Получить номер заказа в карточке')
    def get_id_of_order_card(self):
        return self.get_text(FPL.order_card_id)

    @allure.step('Кликнуть по первому (последнему) заказу в ленте')
    def click_on_order_card(self):
        self.wait_visibility_of_element(FPL.order_in_feed)
        self.click_on_element(FPL.order_in_feed)


