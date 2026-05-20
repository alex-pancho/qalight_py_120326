from api.base_api import BaseAPI

class CarsAPI(BaseAPI):
    def get_all_cars(self):
        return self.get("/cars")

    def get_car_by_id(self, car_id: int):
        return self.get(f"/cars/{car_id}")

    def create_car(self, body: dict):
        return self.post("/cars", json=body)

    def update_car(self, car_id: int, body: dict):
        return self.put(f"/cars/{car_id}", json=body)

    def delete_car(self, car_id: int):
        return self.delete(f"/cars/{car_id}")