import pytest  
from api_client import CarApiClient

@pytest.fixture(scope="session")
def api_client():
    return CarApiClient(base_url="https://fake-car-api.com")


def test_get_all_cars_status_code(api_client):
    response = api_client.get_all_cars()
    assert response.status_code == 200


def test_get_brands_status_code(api_client):
    response = api_client.get_brands()
    assert response.status_code == 200