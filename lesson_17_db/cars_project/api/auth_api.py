from api.base_api import BaseAPI

class AuthAPI(BaseAPI):
    def login(self, email: str, password: str):
        payload = {
            "email": "yevhen@mail.com",
            "password": "qwerty123"
        }
        return self.post("/auth/signin", json=payload)

    def logout(self):
        return self.post("/auth/logout")