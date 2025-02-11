import allure
from locators.main_page_locators import *
from locators.login_page_locators import *
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Возврат текста со страницы создания заказа после перехода по кнопке "Конструктор"')
    def check_constructor_button(self):
        """
        Проверка перехода на страницу создания заказа по кнопке "Конструктор".
        :return: Текст со страницы создания заказа.
        """
        self.element_invisibility(LoginPageLocator.SEARCH_ELEMENT)
        self.click(MainPageLocator.BUTTON_ORDERS_LIST)
        self.element_invisibility(LoginPageLocator.SEARCH_ELEMENT)
        self.click(MainPageLocator.BUTTON_CONSTRUCTOR)
        return self.get_text(MainPageLocator.TEXT_BURGER)

    @allure.step('Переход по кнопке "Лента Заказов"')
    def click_orders_list_button(self):
        """
        Переход на страницу "Лента Заказов" по кнопке.
        """
        self.click(MainPageLocator.BUTTON_ORDERS_LIST)

    @allure.step('Получение списка заказов после перехода по кнопке "Лента Заказов"')
    def check_orders_list_button(self):
        """
        Проверка перехода на страницу "Лента Заказов" и получение текста списка заказов.
        :return: Текст списка заказов.
        """
        self.element_invisibility(LoginPageLocator.SEARCH_ELEMENT)
        self.click(MainPageLocator.BUTTON_ORDERS_LIST)
        return self.get_text(MainPageLocator.TEXT_ORDERS_LIST)

    @allure.step('Переходим по клику на ингредиент и возвращаем детали ингредиента')
    def click_to_ingredient(self):
        """
        Переход к деталям ингредиента по клику на него.
        :return: Текст деталей ингредиента.
        """
        self.element_invisibility(LoginPageLocator.SEARCH_ELEMENT)
        self.click(MainPageLocator.INGREDIENT)
        return self.get_text(MainPageLocator.INGREDIENT_DETAILS)

    @allure.step('Закрываем детали ингредиента и возвращаем текст со страницы создания заказов')
    def click_exit_icon(self):
        """
        Закрытие деталей ингредиента и возврат текста со страницы создания заказов.
        :return: Текст со страницы создания заказов.
        """
        self.element_invisibility(LoginPageLocator.SEARCH_ELEMENT)
        self.click(MainPageLocator.INGREDIENT)
        self.click(MainPageLocator.EXIT_ICON)
        return self.get_text(MainPageLocator.TEXT_BURGER)

    @allure.step('Переносим ингредиент в поле создания бургера')
    def moving_ingredient(self):
        """
        Перемещение ингредиента в поле создания бургера.
        """
        self.element_invisibility(LoginPageLocator.SEARCH_ELEMENT)
        self.moving_element(MainPageLocator.INGREDIENT, MainPageLocator.CREATE_BURGER)

    @allure.step('Проверяем, что после добавления ингредиента, изменился его счётчик')
    def counter_ingredient_increase(self):
        """
        Проверка увеличения счетчика ингредиента после его добавления.
        :return: Текст счетчика ингредиента.
        """
        self.element_invisibility(LoginPageLocator.SEARCH_ELEMENT)
        self.find_element(MainPageLocator.INGREDIENT)
        self.moving_element(MainPageLocator.INGREDIENT, MainPageLocator.CREATE_BURGER)
        return self.get_text(MainPageLocator.COUNTER)

    @allure.step('Оформляем заказ и возвращаем текст, что заказ начали готовить')
    def create_order_auth_user(self):
        """
        Оформление заказа и проверка текста о начале приготовления заказа.
        :return: Текст о начале приготовления заказа.
        """
        self.element_invisibility(LoginPageLocator.SEARCH_ELEMENT)
        self.moving_element(MainPageLocator.INGREDIENT, MainPageLocator.CREATE_BURGER)
        self.click(MainPageLocator.BUTTON_CREATE_ORDER)
        return self.get_text(MainPageLocator.TEXT_SUCCESSFUL)


