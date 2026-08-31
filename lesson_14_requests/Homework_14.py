import requests
import json
from requests.exceptions import HTTPError
from requests.exceptions import ConnectionError
from requests.exceptions import Timeout

response = requests.get("https://jsonplaceholder.typicode.com/posts")



def get_all_posts():
   
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response
print(response.status_code)
print(response.json())
def get_post_by_id(post_id):
    
    url_test = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url_test)
    return response


print("--- Task 1 ---")
resp_all = get_all_posts()

if resp_all.status_code == 200:
    data = resp_all.json()
    print(f"Status: {resp_all.status_code}")
    print(f"Count of records: {len(data)}")
    
   
    if len(data) == 100:
        print("Count check: Pass")
else:
    print("Request error")


print("\n--- Task 2 ---")
target_id = 10
resp_single = get_post_by_id(target_id)

if resp_single.status_code == 200:
    post = resp_single.json()
    print(f"Статус: {resp_single.status_code}")
    
    
    if post.get('id') == target_id:
        print(f"ID meats target ID: {post['id']}")
    
    
    required_fields = ["userId", "id", "title", "body"]
    missing_fields = [field for field in required_fields if field not in post]
    
    if not missing_fields:
        print("All required fiels are present")
    else:
        print(f"Fields are absent: {missing_fields}")
else:
    print(f"Error. Status: {resp_single.status_code}")



def get_todos_by_user(user_id):
  
    url = "https://jsonplaceholder.typicode.com/todos"
   
    params = {'userId': user_id}
    response = requests.get(url, params=params)
    return response



print("--- Task 3 ---")

user_to_check = 2
response = get_todos_by_user(user_to_check)

if response.status_code == 200:
    todos = response.json()
    print(f"Requests delivered: {len(todos)}")

    
    errors = [item for item in todos if item['userId'] != user_to_check]

    if len(errors) == 0:
        print(f"Success: All {len(todos)} belong to {user_to_check}!")
    else:
        print(f"Errot! Found {len(errors)} records another users.")
else:
    print(f"Error requests. Status code: {response.status_code}")



BASE_URL = "https://jsonplaceholder.typicode.com/posts"


print("--- Task 4 ---")
new_post = {
    "title": "My new post",
    "body": "New text",
    "userId": 1
}
response_post = requests.post(BASE_URL, json=new_post)
created_data = response_post.json()

if response_post.status_code == 201:
    print(f"Status 201 (Created): Success")
    assert created_data['title'] == new_post['title']
    assert created_data['body'] == new_post['body']
    print("Data matching!")


print("\n--- Task 5 ---")
updated_post = {
    "id": 5,
    "title": "Updated title",
    "body": "Updated text",
    "userId": 1
}
response_put = requests.put(f"{BASE_URL}/5", json=updated_post)
put_data = response_put.json()

if response_put.status_code == 200:
    print(f"Status 200 (OK): Updated POST")
    print("New data to return:", put_data)


print("\n--- Task 6 ---")
patch_data = {"title": "Only new title"}
response_patch = requests.patch(f"{BASE_URL}/5", json=patch_data)
patched_result = response_patch.json()

if response_patch.status_code == 200:
    print(f"Status 200 (OK): Title changed")
    assert patched_result['title'] == patch_data['title']
    print("New title:", patched_result['title'])


print("\n--- Task 7 ---")
response_delete = requests.delete(f"{BASE_URL}/5")


if response_delete.status_code in [200, 204]:
    print(f"Status {response_delete.status_code}: POST deleted")



BASE_URL = "https://jsonplaceholder.typicode.com/posts"

print("--- Task 8 ---")
response_404 = requests.get(f"{BASE_URL}/999999")

if response_404.status_code == 404:
    print(f"Success:  404 (Not Found)")
elif not response_404.json():
    print("Result: Response delivered")
else:
    print(f" Difference. Status: {response_404.status_code}")



print("\n--- Task 9---")
response_empty = requests.post(BASE_URL, json={})

print(f"API status code: {response_empty.status_code}")
print("Server response:", response_empty.json())



print("\n--- Task 10 ---")
custom_headers = {
    "User-Agent": "QA Student",
    "Content-Type": "application/json"
}

response_headers = requests.get(BASE_URL, headers=custom_headers)

if response_headers.status_code == 200:
    print("Success!")
    
    print("Send User-Agent:", response_headers.request.headers['User-Agent'])





BASE_URL = "https://jsonplaceholder.typicode.com"

def make_request(method, endpoint, **kwargs):
    """
    Універсальна функція для виконання HTTP-запитів.
    :param method: Метод (GET, POST, PUT, PATCH, DELETE)
    :param endpoint: Кінцева точка (наприклад, '/posts')
    :param kwargs: Додаткові аргументи (json, params, headers тощо)
    """
    url = f"{BASE_URL}{endpoint}"
    response = requests.request(method, url, **kwargs)
    return response


import pytest


BASE_URL = "https://jsonplaceholder.typicode.com"

def make_request(method, endpoint, **kwargs):
    url = f"{BASE_URL}{endpoint}"
    return requests.request(method, url, **kwargs)

def test_get_all_posts():
    """Тест перевірки отримання всіх постів"""
    response = make_request("GET", "/posts")
    assert response.status_code == 200, f"Очікували 200, але отримали {response.status_code}"
    assert len(response.json()) == 100

def test_get_single_post():

    response = make_request("GET", "/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1
    assert 'title' in data

def test_create_post():
   
    payload = {"title": "QA", "body": "Testing", "userId": 1}
    response = make_request("POST", "/posts", json=payload)
    assert response.status_code == 201
    assert response.json()['title'] == "QA"

def test_delete_post():
   
    response = make_request("DELETE", "/posts/1")
    assert response.status_code in [200, 204]
