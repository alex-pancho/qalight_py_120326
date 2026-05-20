import requests

class BaseAPI:

    BASE_URL = "https://qauto.forstudy.space/api"

    def __init__(self, session: requests.Session):
        self.session = session

    def get(self, endpoint: str, params=None):
        return self.session.get(f"{self.BASE_URL}{endpoint}", params=params)
    
    def post(self, endpoint: str, json=None):
        return self.session.post(f"{self.BASE_URL}{endpoint}", json=json)
    
    def put(self, endpoint: str, json=None):
        return self.session.put(f"{self.BASE_URL}{endpoint}", json=json)

    def delete(self, endpoint: str):
        return self.session.delete(f"{self.BASE_URL}{endpoint}")