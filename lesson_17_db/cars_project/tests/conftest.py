import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import pytest
import requests
from api.api_manager import APIManager

@pytest.fixture
def api():

    session = requests.Session()
    api = APIManager(session)
    response = api.auth.login(
        email="test_user@mail.com",
        password="123456"
    )

    assert response.status_code == 200, f"Login failed: {response.text}"
    return api