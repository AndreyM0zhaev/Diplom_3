from selenium.webdriver.common.by import By

class Locators:
    REG_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]") # Кнопка Войти в аккаунт
    REG_LINK = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]") # Ссылка Зарегистрироваться
    RECOVERY_LINK = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]") # Ссылка Восстановить пароль
    NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name' and @type='text']") # Поле ввода Имя
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name' and @type='text']") # Поле ввода Email
    PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input[@name='Пароль' and @type='password']") # Поле ввода Пароль
    AUTH_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") # Кнопка Войти
    AUTH_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj']") # Ссылка "Войти"
    PERS_ACC_INTO_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]") # Кнопка Личный Кабинет
    PERS_ACC_LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]") # Кнопка Выход
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]") # Кнопка Конструктор
    CONSTRUCTOR_BURGER_SECTION = (By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']") # Заголовок секции Соберите бургер
    LOGO_BUTTON = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a") # Логотип Stellar Burgers
    LINK_FILLINGS = (By.XPATH, "//span[contains(text(),'Начинки')]") # Вкладка Начинки
    HEADER_FILLING = (By.XPATH,"//h2[contains(text(),'Начинки')]") # Заголовок вкладки Начинки
    LINK_SAUCES = (By.XPATH, "//span[contains(text(),'Соусы')]") # Вкладка Соусы
    HEADER_SAUCES = (By.XPATH, "//h2[contains(text(),'Соусы')]") # Заголовок вкладки Соусы
    LINK_BUNS = (By.XPATH, "//span[contains(text(),'Булки')]") # Вкладка Булки
    HEADER_BUNS = (By.XPATH, "//h2[contains(text(),'Булки')]") # Заголовок вкладки Булки
    ALERT_INVALID_PASS = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]") # Уведомление о некорректном пароле
