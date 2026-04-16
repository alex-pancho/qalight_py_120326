import pytest


@pytest.fixture
def default_user():
    # Підготовка даних
    user = {"name": "Ivan", "role": "admin", "balance": 100}
    return user
