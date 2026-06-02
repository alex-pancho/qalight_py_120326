import pytest

@pytest.mark.data
def test_missing_values():
    pass

@pytest.mark.user
def test_income_contribution():
    pass

@pytest.mark.cart
def test_gender_parity():
    pass

# Патерн: Arrange — Act — Assert (AAA)
def test_high_risk_job():
    # Arrange — готуємо дані
    my_dict = {"військо": {"age": 25, "income": 25000}}

    # Act — виконуємо дію
    # user_in_database = requests.get(url).json()
    user_in_database = {"Jonh": {"age": 20, "income": 25000, "title": "військо"}}

    jonh_salary = user_in_database["Jonh"]["income"]
    jonh_job_title = user_in_database["Jonh"]["title"]
    # Assert — перевіряємо результат
    expected_max_salary = my_dict[jonh_job_title]["income"]
    assert jonh_salary >= expected_max_salary

