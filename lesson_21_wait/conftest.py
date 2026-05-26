import pytest
from selenium.webdriver import Firefox, Chrome, FirefoxOptions, ChromeOptions

def firefox(debug=False):
    # Ініціалізуємо параметри для веб-драйвера Firefox
    options = FirefoxOptions()
    options.add_argument("--headless")  # Запуск у безголовному режимі
    # (без відображення вікна браузера)

    # Вибираємо, чи потрібно запускати драйвер у режимі налагодження (debug mode)
    driver = Firefox() if debug else \
             Firefox(options=options)
    # Використання headless, якщо не включено налагодження

    # Максимізуємо вікно браузера (якщо відображення не вимкнено)
    driver.maximize_window()

    # Повертаємо об'єкт драйвера
    return driver


@pytest.fixture(scope="session")
def driver():
    driver = firefox()
    yield driver
    driver.close()


@pytest.fixture(scope="session")
def url():
    return "http://localhost:8000"
