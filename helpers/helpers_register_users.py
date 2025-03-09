from faker import Faker

faker = Faker()

class User:

# Метод генерации данных для регистрации произвольного пользователя
    @staticmethod
    def registration_new_user():
        user_name = faker.name()
        user_email = faker.email()
        user_password = faker.password()
        user_data = {"email": user_email, "password": user_password, "name": user_name}
        return user_data
