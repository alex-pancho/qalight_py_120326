import pytest

def test_get_all_cars_status_code(api):
    response = api.cars.get_all_cars()

    assert response.status_code == 200

def test_get_all_cars_response_contains_data(api):
    response = api.cars.get_all_cars()
    body = response.json()

    assert "data" in body

def test_get_all_cars_returns_list(api):
    response = api.cars.get_all_cars()
    body = response.json()

    assert isinstance(body["data"], list)

def test_create_car_status_code(api):
    payload = {
        "brand": "BMW",
        "model": "X5",
        "mileage": 100
    }

    response = api.cars.create_car(payload)

    assert response.status_code == 201

def test_create_car_response_contains_correct_mileage(api):
    payload = {
        "brand": "Audi",
        "model": "A6",
        "mileage": 150
    }

    response = api.cars.create_car(payload)
    body = response.json()
    
    assert body["data"]["mileage"] == 150