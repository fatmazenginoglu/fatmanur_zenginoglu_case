import requests

class UserAPI:
    def __init__(self, base_url="https://petstore.swagger.io/v2"):
        self.base_url = base_url

    def create_user(self, user_data):
        """Yeni bir kullanıcı oluştur"""
        url = f"{self.base_url}/user"
        return requests.post(url, json=user_data)

    def create_users_with_list(self, users):
        """Bir liste halinde kullanıcılar oluşturur."""
        url = f"{self.base_url}/user/createWithList"
        return requests.post(url, json=users)

    def create_users_with_array(self, users):
        """Kullanıcıları toplu olarak oluşturma"""
        url = f"{self.base_url}/user/createWithArray"
        return requests.post(url, json=users)

    def get_user_by_username(self, username):
        """Belirtilen kullanıcı adına sahip kullanıcıyı getirir."""
        url = f"{self.base_url}/user/{username}"
        return requests.get(url)

    def update_user_by_username(self, username, user_data):
        """Belirtilen kullanıcı adına sahip kullanıcıyı günceller."""
        url = f"{self.base_url}/user/{username}"
        return requests.put(url, json=user_data)

    def delete_user_by_username(self, username):
        """Belirtilen kullanıcıyı siler."""
        url = f"{self.base_url}/user/{username}"
        return requests.delete(url)

    def login_user(self, username, password):
        """Kullanıcı girişi yapar."""
        url = f"{self.base_url}/user/login"
        params = {"username": username, "password": password}
        return requests.get(url, params=params)

    def logout_user(self):
        """Kullanıcı oturumunu kapatma"""
        return requests.get(f"{self.base_url}/user/logout")
