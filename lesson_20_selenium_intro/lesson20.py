from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# Ініціалізація веб-драйвера для Chrome
driver = webdriver.Firefox()

# Відкриття веб-сторінки
driver.get("http://localhost:8000")

# user_field = driver.find_element(By.ID, "username")
# pass_field = driver.find_element(By.ID, "password")
# login_button = driver.find_element(By.ID, "login_button")

# user_field = driver.find_element(By.CSS_SELECTOR, ".input-field#username")
# pass_field = driver.find_element(By.CSS_SELECTOR, ".input-field#password")
# login_button = driver.find_element(By.CSS_SELECTOR, "#login_button")

user_field = driver.find_element(By.XPATH, "//input[@id='username']")
pass_field = driver.find_element(By.XPATH, "//input[@id='password']")
login_button = driver.find_element(By.XPATH, "//button[@id='login_button']")

li_el2 = driver.find_element(By.XPATH, "//li[.='Елемент списку 2']") # text()='Елемент списку 2'

li_elements = driver.find_elements(By.TAG_NAME, "li")
    
# Пошук конкретного елемента серед отриманих
for li in li_elements:
    # пошук може бути повiльним якщо елементiв багато
    if li.text == "Елемент списку 2":
        # Знайдено потрібний елемент
        print("Знайдено елемент:", li.text)
        break


# Робота з веб-елементами і виконання дій на сторінці
sleep(7)

# Закриття браузера
driver.quit()