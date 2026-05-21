from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common import NoSuchElementException

from time import sleep

def get_browser(chrome:bool=True):
    """
    This return browser engine
    """
    if chrome:
        return webdriver.Chrome()
    else:
        return webdriver.Firefox()

def find_element_by_xpath(driver: webdriver, locator: str):
    try:
        return driver.find_element(By.XPATH, locator)
    except NoSuchElementException as e:
        print("not found!", e.msg)
        return

def proc_elements_page():
    driver = get_browser()
    driver.get("http://localhost:8000/action.html")
    username_xpath = "//input[@id='username']"
    password_xpath = "//input[@id='password']"
    male_radio_xpath = "//*[@id='male']"
    newsletter_checkbox_xpath = "//*[@id='newsletter']"
    country_dropdown_xpath = "//*[@id='country']"
    submit_button_xpath = "//*[@id='submit']"

    username_field = find_element_by_xpath(driver, username_xpath)
    username_field.send_keys("example_username")

    password_field = find_element_by_xpath(driver, password_xpath)
    password_field.send_keys("example_password")

    male_radio = find_element_by_xpath(driver, male_radio_xpath)
    male_radio.click()

    newsletter_checkbox = find_element_by_xpath(driver, newsletter_checkbox_xpath)
    newsletter_checkbox.click()

    country_dropdown_find = find_element_by_xpath(driver, country_dropdown_xpath)
    country_dropdown = Select(country_dropdown_find)
    country_dropdown.select_by_visible_text("США")

    submit_button = find_element_by_xpath(driver, submit_button_xpath)
    submit_button.click()


if __name__ == "__main__":
    proc_elements_page()
    sleep(3)
