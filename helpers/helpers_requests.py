# import allure
# import requests
#
#
# class Api:
#     # URL-адрес сервера
#     SERVER_URL = 'https://stellarburgers.nomoreparties.site'
#
#     # Эндпойнты (ручки) запросов к API
#     API_CREATE_USER = '/api/auth/register'  # Регистрация пользователя: POST '/api/auth/register'
#     API_DELETE_USER = '/api/auth/user'  # Удаление пользователя: DELETE '/api/auth/user'
#     # headers={"Authorization": "{auth_token}"}
#
#
# class HelpersRequests:
#
#     @staticmethod
#     @allure.step('Отправляем API-запрос на создание пользователя')
#     def request_create_user(payload):
#         request_url = f'{Api.SERVER_URL}{Api.API_CREATE_USER}'
#         response = requests.post(f'{request_url}', json=payload)
#         return response
#
#     @staticmethod
#     @allure.step('Отправляем API-запрос на удаление пользователя')
#     def request_delete_user(headers):
#         request_url = f'{Api.SERVER_URL}{Api.API_DELETE_USER}'
#         response = requests.delete(f'{request_url}', headers=headers)
#         return response



from data import *
import requests
import allure


class Order:

    @allure.step('Создание нового заказа пользователя через API')
    def create_order(self, create_user):
        token = create_user[1].json().get("accessToken")
        headers = {'Authorization': token}
        with allure.step("Отправка запроса на создание заказа"):
            response = requests.post(
                f"{BASE_URL}{CREATE_ORDER}",
                headers=headers,
                data=valid_ingredients
            )

        # Можно добавить обработку ошибок, чтобы удостовериться, что заказ был успешно создан
        if response.status_code != 201:
            raise Exception(f"Не удалось создать заказ. Статус: {response.status_code}, Ответ: {response.text}")




    @allure.step('Получение заказов пользователя через API')
    def get_user_orders(self, create_user):

        token = create_user[1].json().get("accessToken")
        headers = {'Authorization': token}

        # Отправка GET запроса для получения списка заказов
        response = requests.post(
            f"{BASE_URL}{CREATE_ORDER}",
            headers=headers,
        )

        # Проверка на успешный ответ и наличие заказов
        if response.status_code != 200:
            raise Exception(f"Не удалось получить заказы. Статус: {response.status_code}, Ответ: {response.text}")

        orders = response.json().get("orders", [])
        if not orders:
            raise Exception("У пользователя нет заказов.")

        # Возвращаем номер первого заказа
        return orders[0]["number"]
