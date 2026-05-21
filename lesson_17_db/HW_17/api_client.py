import requests

from endpoints import CarEndpoints

class CarApiClient:
    def __init__(self, base_url="https://car-api.com"): 
       
        self.base_url = base_url
        self.session = requests.Session()

    def get_all_cars(self):
        
        url = f"{self.base_url}{CarEndpoints.CARS}"
        response = self.session.get(url)
        return response

    def get_brands(self):
        
        url = f"{self.base_url}{CarEndpoints.BRANDS}"
        response = self.session.get(url)
        return response