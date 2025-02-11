from selenium.webdriver.common.by import By


class MainPageLocator:
    # Локаторы для кнопок и текста на главной странице
    BUTTON_CONSTRUCTOR = [By.XPATH, ".//p[contains(text(), 'Конструктор')]"]  # Кнопка "Конструктор"
    BUTTON_ORDERS_LIST = [By.XPATH, ".//p[contains(text(), 'Лента Заказов')]"]  # Кнопка "Лента Заказов"
    TEXT_BURGER = [By.XPATH, ".//h1[contains(text(), 'Соберите бургер')]"]  # Текст "Соберите бургер"
    TEXT_ORDERS_LIST = [By.XPATH, ".//h1[contains(text(), 'Лента заказов')]"]  # Текст "Лента заказов"

    # Локаторы для работы с ингредиентами
    INGREDIENT = [By.XPATH, ".//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa6d')]"]  # Ингредиент
    INGREDIENT_DETAILS = [By.XPATH, ".//h2[text()='Детали ингредиента']"]  # Заголовок деталей ингредиента
    EXIT_ICON = [By.XPATH, ".//button[@type='button']"]  # Иконка закрытия деталей ингредиента

    # Локаторы для создания бургера
    CREATE_BURGER = [By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]"]  # Поле создания бургера
    COUNTER = [By.XPATH, ".//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa6d')]"
               "//ancestor::p[contains(@class, 'counter_counter')]"]  # Счетчик ингредиента

    # Локаторы для оформления заказа
    BUTTON_CREATE_ORDER = [By.XPATH, ".//button[text()='Оформить заказ']"]  # Кнопка "Оформить заказ"
    TEXT_SUCCESSFUL = [By.XPATH, ".//p[text()='Ваш заказ начали готовить']"]  # Текст успешного оформления заказа
    BUTTON_CLOSE_ORDER = [By.XPATH, ".//button[contains(@class, 'Modal_modal__close_modified')]"]  # Кнопка закрытия заказа

    # Локаторы для номера заказа
    NUMBER_ORDER = [By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow')]"]  # Номер заказа