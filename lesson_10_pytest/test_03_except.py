import pytest
from app.bank import (
    calculate_discount,
)


# Тестуємо класи еквівалентності
def test_vip_discount():
    assert calculate_discount(100, "VIP") == 80


def test_student_discount():
    assert calculate_discount(100, "Student") == 90


def test_no_discount():
    assert calculate_discount(100, "Regular") == 100


# Граничні значення
def test_zero_price():
    assert calculate_discount(0, "VIP") == 0

def test_small_price():
    actual_result = calculate_discount(0.01, "Student")
    assert round(actual_result, 3) == 0.009 # НЕ ПОРІВНЮВАТИ НАПРЯМУ! ТІЛЬКИ З round()

# Тест на помилку
def test_negative_price_error():
    # Перевіряємо, що при ціні -100 виникне помилка ValueError
    with pytest.raises(ValueError) as excinfo:
        calculate_discount(-1, "VIP")
    # Можна також перевірити текст повідомлення в помилці
    assert str(excinfo.value) == "Price can not less than 0"


@pytest.mark.parametrize(
        "category, expected_pirce",
        [("VIP", 80),
        ("Student", 90),
        ("other", 100),]
)
def test_discount_params(category, expected_pirce):
    #category = "VIP", expected_pirce = 80
    assert calculate_discount(100, category) == expected_pirce

def test_user(default_user):
    assert default_user["name"] == "Ivan"
    assert default_user["balance"] > 0
    assert default_user["role"] in ["admin", "user"]
    default_user["name"] = "Sanya"
    assert default_user["name"] == "Sanya"


def test_user_2(default_user):
    assert default_user["name"] == "Ivan"
    assert default_user["balance"] > 0
    assert default_user["role"] in ["admin", "user"]
