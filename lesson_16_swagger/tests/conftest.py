import pytest
import os
import requests
from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:5000")

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def session():
    return requests.Session()

@pytest.fixture
def valid_user():
    return (
        os.getenv("FL_USERNAME"),
        os.getenv("PASSWORD")
    )