import allure
from selenium.webdriver.common.by import By


class FeedPageLocators:
    """
    Локаторы для тестов списка заказов.
    """
    BUTTON_ORDER = [By.XPATH, ".//li[1][contains(@class, 'OrderHistory_listItem')]"]  # Кнопка заказа в списке
    COMPOUND = [By.XPATH, ".//p[text()='Cостав']"]  # Текст "Состав" в деталях заказа
    COMPLETED_ALL_TIME = [By.XPATH, ".//p[text()='Выполнено за все время:']//"
                                    "following::p[1][contains(@class, 'OrderFeed_number')]"]  # Количество выполненных заказов за все время
    COMPLETED_TODAY = [By.XPATH, ".//p[text()='Выполнено за сегодня:']//"
                                 "following::p[contains(@class, 'OrderFeed_number')]"]  # Количество выполненных заказов за сегодня
    IN_PROGRESS = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]//li[1]"]  # Заказ в процессе выполнения
    FEED_NAME = [By.XPATH, ".//h2[text()='Флюоресцентный бургер']"]  # Название заказа