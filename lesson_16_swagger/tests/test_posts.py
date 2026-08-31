import requests

def test_home_response_not_empty(base_url):
    response = requests.get(base_url)
    assert len(response.text) > 0, "Response is empty"

def test_home_content_type(base_url):
    response = requests.get(base_url)
    assert "text/html" in response.headers.get("Content-Type", ""), "Response isn't html"

def test_register_page_content_type(base_url):
    response = requests.get(f"{base_url}/register")
    assert "text/html" in response.headers.get("Content-Type", ""), "Response isn't html"

def test_login_page_content_type(base_url):
    response = requests.get(f"{base_url}/login")
    assert "text/html" in response.headers.get("Content-Type", ""), "Response isn't html"