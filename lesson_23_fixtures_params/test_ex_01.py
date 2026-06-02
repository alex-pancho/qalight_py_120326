import requests


def test_get_user_returns_200(BASE_URL, user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")

    assert response.status_code == 200


def test_get_user_contains_expected_fields(BASE_URL, user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")

    body = response.json()

    assert "id" in body
    assert "name" in body
    assert "email" in body


def test_get_user_returns_correct_id(BASE_URL, user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")

    body = response.json()

    assert body["id"] == user_id

def test_model(model):
    assert model is None