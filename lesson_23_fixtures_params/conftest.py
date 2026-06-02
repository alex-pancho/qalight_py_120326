import pytest

@pytest.fixture(scope="session")
def BASE_URL():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def user_id():
    return 1

@pytest.fixture(scope="session")
def dataset():
    return #load_data("users.csv")

@pytest.fixture(scope="module")
def model(dataset):
    return #train_model(dataset)
