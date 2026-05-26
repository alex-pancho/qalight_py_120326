# EXplicit for EXist
# IMplicit for IMaginary

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def example_with_implicit_wait(driver):
    browser = driver
    browser.implicitly_wait(10)  # Чекати не більше 10 секунд

    browser.get("https://www.example.com")

    # Знаходимо елемент на сторінці
    heading = browser.find_element(By.TAG_NAME,"h1")

    # Перевіряємо, чи вірний текст заголовку
    assert heading.text == "Example Domain"


def test_example_with_explicit_wait(driver: webdriver, url):
    driver.get(url)

    headline_locator = (By.XPATH, "//h2")
    login_input_locator = (By.XPATH, '//*[@id="username"]')
    password_input_locator = (By.XPATH, '//*[@id="password"]')
    button_locator = (By.XPATH, '//button[@onclick="login()"]')

    # Чекаємо, поки заголовок сторінки з'явиться (не більше 10 секунд)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(headline_locator),
        "element not found"
        )
    # EC.visibility_of_element_located
    # EC.element_to_be_clickable
    # EC.text_to_be_present_in_element
    # EC.title_contains


    # Знаходимо елемент на сторінці після очікування
    headline = driver.find_element(*headline_locator) #By.TAG_NAME,"h1"
    login_input = driver.find_element(*login_input_locator)
    password_input = driver.find_element(*password_input_locator)
    button = driver.find_element(*button_locator)


    # Перевіряємо, чи вірний текст заголовку
    assert "Автосервіс" in headline.text, "Head text is unexpected"
    login_input.send_keys("hello")
