import requests

def test_home_page_status_code(base_url):
    response = requests.get(base_url)
    assert response.status_code == 200, "Wrong status code"

def test_home_page_contains_html(base_url):
    response = requests.get(base_url)
    assert "html" in response.text.lower(), "No html markers found"