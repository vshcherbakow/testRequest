import requests
from utils.api import UserAPI
import re

base_url = "https://jsonplaceholder.typicode.com"
user_api = UserAPI(base_url)


def test_get_users_status_code():
    """Проверка статус кода на 200."""
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200
    print('Статус код 200')


def test_get_users_not_empty():
    """Проверка, что список пользователей не пустой."""
    users = user_api.get_users_list()
    assert users
    print('Список не пустой')


def test_get_users_structure():
    """Проверка структуры каждой записи пользователя."""
    users = user_api.get_users_list()
    required_fields = {"id", "name", "username", "email"}

    for user in users:
        assert required_fields.issubset(user.keys())
    print('Пользователи имеют все необходимые поля')

def test_email_format():
    """Проверка формата email для каждого пользователя."""
    users = user_api.get_users_list()
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    for user in users:
        email = user["email"]
        assert re.match(email_pattern, email), f"Email '{email}' имеет неправильный формат."
    print('Email верный')