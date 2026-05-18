import requests

def test_register_page_available(base_url: str):
    response = requests.get(f"{base_url}/register")
    assert response.status_code == 200, "Wrong status code"

def test_login_page_available(base_url: str):
    response = requests.get(f"{base_url}/login")
    assert response.status_code == 200, "Wrong status code"

def test_non_existing_page_returns_404(base_url: str):
    response = requests.get(f"{base_url}/this-mock_page-does-not-exist")
    assert response.status_code == 404, "Wrong status code"