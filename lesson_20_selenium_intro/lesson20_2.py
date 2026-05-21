from time import sleep
from lesson20_1 import get_browser, find_element_by_xpath


driver = get_browser()
driver.get("http://localhost:8000/frame.html")
frame_xpath = "//*[@id='myFrame']"
frame = find_element_by_xpath(driver, frame_xpath)

# Перемикаємося до фрейму
driver.switch_to.frame(frame)
frame_button_xpath = "//*[@id='myButton']"

frame_button = find_element_by_xpath(driver, frame_button_xpath)
for _ in range(3):
    frame_button.click()
    sleep(2)

sleep(3)
