from api.auth_api import AuthAPI
from api.cars_api import CarsAPI

class APIManager:
    def __init__(self, session):
        self.auth = AuthAPI(session)
        self.cars = CarsAPI(session)