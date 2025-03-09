from pages.base_page import *
from locators.feed_page_locators import FeedPageLocators as FPL
from locators.login_page_locators import LoginPageLocator as LPL



class FeedPage(BasePage):

    @allure.step('Получаем список элементов страницы со счетчиком "Выполнено за всё время"')
    def get_list_orders_completed_all_time(self):
        elements = self.wait_for_load_all_elements(FPL.COMPLETED_ALL_TIME)
        return elements

    @allure.step('Получаем список элементов страницы со счетчиком "Выполнено за сегодня"')
    def get_list_orders_completed_today(self):
        elements = self.wait_for_load_all_elements(FPL.COMPLETED_TODAY)
        return elements

    @allure.step('Получение количества заказов за все время')
    def get_orders_completed_all_time(self):
        elements = self.get_list_orders_completed_all_time()
        return int(str(elements[0].text))

    @allure.step('Получение количества заказов за сегодня')
    def get_orders_completed_today(self):
        elements = self.get_list_orders_completed_today()
        return int(str(elements[0].text))

    @allure.step('Получение номера заказа "В процессе"')
    def get_number_in_progress(self):
        self.element_invisibility(LPL.SEARCH_ELEMENT)
        self.wait_for_changed_text(FPL.IN_PROGRESS, 'Все текущие заказы готовы!')
        return self.get_text(FPL.IN_PROGRESS)

    @allure.step('Получение названия заказа из Ленты Заказов')
    def get_feed_name_from_order_list(self):
        self.element_invisibility(LPL.SEARCH_ELEMENT)
        return self.get_text_on_element(FPL.FEED_NAME)

    @allure.step('Кликнуть по первому (последнему) заказу в ленте')
    def click_on_order_card(self):
        self.wait_visibility_of_element(FPL.ORDER_IN_FEED)
        self.click_on_element(FPL.ORDER_IN_FEED)



