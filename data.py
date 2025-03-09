# Данные пользователя для авторизации и регистрации

EMAIL = 'Mozhaev.Andrey.v@yandex.ru'  # Email пользователя
PASSWORD = 'asdfgh123456!'  # Пароль пользователя


CREATE_USER = '/api/auth/register'
DELETE_USER = '/api/auth/user'
CREATE_ORDER = '/api/orders'

# Данные для оформления заказа
valid_ingredients = {
    "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
}

# Базовые URL для тестирования
BASE_URL = 'https://stellarburgers.nomoreparties.site'  # Основной URL сайта
LOGIN_URL = 'https://stellarburgers.nomoreparties.site/login'  # URL страницы входа
PASSWORD_RECOVERY_URL = 'https://stellarburgers.nomoreparties.site/forgot-password'  # URL страницы восстановления пароля
ORDERS_LIST_URL = 'https://stellarburgers.nomoreparties.site/feed'  # URL страницы ленты заказов

# Текстовые константы для проверок
BURGER = 'Соберите бургер'  # Текст на странице создания заказа
FEED = 'Лента заказов'  # Текст на странице ленты заказов
DETAILS = 'Детали ингредиента'  # Текст в деталях ингредиента
X2 = '2'  # Значение счетчика ингредиента
IN_PROGRESS = 'Ваш заказ начали готовить'  # Сообщение о начале приготовления заказа

# Константы с описанием
PROFILE_TEXT = "Профиль"  # Ожидаемый текст для раздела "Профиль"
PRODUCT_TEXT = "Флюоресцентный бургер"  # Ожидаемый текст для названия продукта
LOG_IN_TEXT = "Войти"  # Ожидаемый текст для кнопки "Войти"

RECOVERY_TEXT = 'Восстановить'
PASSWORD_RECOVERY_TEXT = 'Восстановление пароля'
