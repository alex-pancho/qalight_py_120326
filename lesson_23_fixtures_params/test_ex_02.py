import pytest
# def test_income_low(model):
#     p = model.predict_proba([["IT", 25, 10000]])[0][1]
#     assert p > 0.1

# def test_income_medium(model):
#     p = model.predict_proba([["IT", 25, 30000]])[0][1]
#     assert p > 0.1

@pytest.mark.parametrize("income", [10000, 20000, 30000, 40000])
def test_income_range(income):
    assert income > 9000


@pytest.mark.parametrize("job, income", [
    ("IT",      50000),
    ("IT",      70000),
    ("спорт",   25000),
    ("військо", 15000),
])
def test_job_income_combo(job, income):
    jobs = ("IT", "спорт", "військо",)
    assert job in jobs and income > 9000

@pytest.mark.skip(reason="модель ще не готова")
def test_something():
    pass

@pytest.mark.xfail(reason="відомий баг у версії 1.0")
def test_known_issue():
    assert True
