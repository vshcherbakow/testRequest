import requests

class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_users_list(self):
        '''Получить список всех пользователей'''
        response = requests.get(f'{self.base_url}/users')
        return response.json()



