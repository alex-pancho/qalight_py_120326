# Лекція: Патерни та декоратори у pytest. Параметризовані тести. Звіти.

## Контекст: навіщо це потрібно в тестуванні

Коли ми тестуємо, ми часто хочемо перевірити одну й ту саму поведінку для **набору вхідних значень**. Наприклад:

- чи коректно API обробляє різні рівні навантаження та чи не зростає кількість помилок при збільшенні кількості запитів
- чи однаково коректно працюють API responses для різних типів даних і edge cases
- чи правильно система працює для різних ролей користувачів в UI
- чи немає UI/API inconsistencies для користувачів з різних країн, мов або регіональних налаштувань


Робити окремий тест для кожного випадку — погана ідея. Тут на допомогу приходять **параметризовані тести** та **фікстури**.

## 1. Фікстури (`@pytest.fixture`)

### Що це

Фікстура — це функція, яка **готує дані або об'єкти** для тестів. Вона виконується **один раз** і передається у тест як аргумент.

```python
import pytest

@pytest.fixture
def BASE_URL():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def user_id():
    return 1
```

```python
import requests


def test_get_user_returns_200(BASE_URL, user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")

    assert response.status_code == 200
```

```python
import requests


def test_get_user_contains_expected_fields(BASE_URL, user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")

    body = response.json()

    assert "id" in body
    assert "name" in body
    assert "email" in body
```

```python
import requests


def test_get_user_returns_correct_id(BASE_URL, user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")

    body = response.json()

    assert body["id"] == user_id
```

pytest сам розуміє, що `BASE_URL` і `user_id` — це фікстури. Нічого додатково імпортувати не потрібно.

### Параметр `scope`

За замовчуванням фікстура виконується **перед кожним тестом**. Але у цілому ряді випадків це не має сенсу.
Параметр дозволяє рідше запускати фікстуру.

```python
@pytest.fixture(scope="session")
def model():
    # виконається ОДИН раз для всієї сесії
    return action(dataset)
```

| scope | коли виконується |
|---|---|
| `function` | перед кожним тестом (за замовчуванням) |
| `module` | один раз на файл |
| `session` | один раз на весь запуск |

У тестуванні API `scope="session"` часто використовують — наприклад, щоб не створювати нову HTTP-сесію або токен авторизації перед кожним тестом, бо це уповільнює виконання тестів.

### `conftest.py` — спільне місце для фікстур

Якщо кілька тестових файлів використовують одні й ті самі фікстури, їх виносять у файл `conftest.py`. pytest знаходить його **автоматично**.

```
project/
├── conftest.py          ← спільні фікстури
├── test_data.py
├── test_model.py
```

```python
# conftest.py
import pytest
from model_builder import train_model
from data_loader import load_data

@pytest.fixture(scope="session")
def dataset():
    return load_data("users.csv")

@pytest.fixture(scope="session")
def model(dataset):
    return train_model(dataset)
```

Зверніть увагу: фікстура `model` **приймає** фікстуру `dataset` як аргумент. Це ланцюжок залежностей.

## 2. Параметризовані тести (`@pytest.mark.parametrize`)

### Проблема

Ось погана практика — копіювати тест для кожного значення:

```python
def test_income_low(model):
    p = model.predict_proba([["IT", 25, 10000]])[0][1]
    assert p > 0.3

def test_income_medium(model):
    p = model.predict_proba([["IT", 25, 30000]])[0][1]
    assert p > 0.1

def test_income_high(model):
    ...
```

Це важко підтримувати і погано читається.

### Рішення: `@pytest.mark.parametrize`

```python
@pytest.mark.parametrize("income", [10000, 20000, 30000, 40000])
def test_income_range(model, income):
    row = ["IT", 25, income]
    result = model.predict([row])[0]
    assert result in [0, 1]
```

pytest запустить цей тест **4 рази** — по одному для кожного значення.

### Кілька параметрів

```python
@pytest.mark.parametrize("job, income", [
    ("IT",      50000),
    ("спорт",   25000),
    ("військо", 15000),
])
def test_job_income_combo(model, job, income):
    row = [job, 30, income]
    result = model.predict([row])[0]
    assert result in [0, 1]
```

## 3. Маркери (`@pytest.mark`)

Маркери дозволяють **групувати та фільтрувати** тести.

### Вбудовані маркери

```python
@pytest.mark.skip(reason="модель ще не готова")
def test_something():
    ...

@pytest.mark.xfail(reason="відомий баг у версії 1.0")
def test_known_issue():
    ...
```

`xfail` — тест очікується неуспішним. Якщо він раптом пройде — pytest позначить це як `XPASS` (несподіваний успіх).

### Власні маркери

Можна визначити свої маркери для категоризації тестів:

```python
# pytest.ini або pyproject.toml
[pytest]
markers =
    data: тести якості даних
    model: тести поведінки моделі
    bias: тести на упередженість
```

```python
@pytest.mark.data
def test_missing_values(dataset):
    ...

@pytest.mark.model
def test_income_contribution(model):
    ...

@pytest.mark.bias
def test_gender_parity(dataset):
    ...
```

Запуск лише певної групи:

```bash
pytest -m data        # тільки тести даних
pytest -m "not bias"  # все крім bias-тестів
```

## 4. Патерни організації тестів

### Патерн: Arrange — Act — Assert (AAA)

Кожен тест будується з трьох частин:

```python
def test_high_risk_job(model):
    # Arrange — готуємо дані
    row = ["військо", 25, 15000]

    # Act — виконуємо дію
    risk = model.predict_proba([row])[0][1]

    # Assert — перевіряємо результат
    assert risk > 0.5
```

Цей патерн робить тести **читабельними** навіть для людей без досвіду програмування.

### Патерн: Boundary Testing

Перевіряємо поведінку **на межах** значень:

```python
@pytest.mark.parametrize("age", [18, 19, 24, 25, 26])
def test_age_boundary(model, age):
    row = ["IT", age, 30000]
    result = model.predict([row])[0]
    assert result in [0, 1]
```

Молодші за 25 — вища ймовірність ризику. Тест перевіряє, що межа обробляється коректно.

### Патерн: Negative Testing

Що відбувається при **некоректних вхідних даних**:

```python
def test_model_with_zero_income(model):
    row = ["IT", 30, 0]
    result = model.predict([row])[0]
    assert result in [0, 1]  # модель не повинна падати
```

## 5. Звіти про тестування

### Базовий запуск

```bash
pytest
```

Виведення:

```
test_data.py::test_missing_values PASSED
test_data.py::test_outliers FAILED
test_model.py::test_income_contribution[10000-30000] PASSED
test_model.py::test_income_contribution[20000-50000] PASSED
```

Кожна параметризована комбінація — окремий рядок у звіті.

### Детальний вивід

```bash
pytest -v          # verbose — детальні назви
pytest -v -s       # + виводить print() та логи
```

### HTML-звіт (`pytest-html`)

Pytest дозволяє генерувати красивий HTML-звіт із результатами тестів за допомогою плагіна `pytest-html`.

Встановлення:

```bash
pip install pytest-html
```

Запуск тестів із генерацією звіту:

```bash
pytest --html=report.html
```

Після виконання тестів буде створений файл `report.html`, який можна відкрити у браузері.

У звіті зазвичай міститься:

* кількість passed / failed / skipped тестів
* час виконання
* stack trace для помилок
* назви тестів
* додаткові логи або screenshots (якщо налаштовано)

Це особливо зручно для:

* QA-звітності
* демонстрації результатів команді
* CI/CD pipeline
* збереження історії запусків

Також часто використовують:

```bash
pytest --html=report.html --self-contained-html
```

Опція `--self-contained-html` створює один повністю автономний HTML-файл без зовнішніх залежностей.

### Звіт у форматі JUnit XML

Pytest підтримує генерацію XML-звіту у форматі JUnit, який часто використовується в CI/CD системах.

Команда:

```bash
pytest --junitxml=results.xml
```

Після запуску створиться файл `results.xml`.

Такий формат читають:

* Jenkins
* GitLab CI/CD
* GitHub Actions
* Azure DevOps
* TeamCity та інші CI системи

У XML-звіті зберігається:

* список тестів
* статус кожного тесту
* помилки та exception messages
* час виконання

Приклад використання в CI:

```bash
pytest tests/ --junitxml=reports/results.xml
```

CI-система може автоматично:

* показувати статистику тестів
* будувати графіки
* позначати failed tests
* зберігати історію запусків

Для automation QA це стандартний спосіб інтеграції тестів у pipeline.


Стандартний формат для CI/CD систем (GitHub Actions, GitLab CI).

### Кількість успішних/неуспішних тестів

```bash
pytest -q   # коротке зведення
```

```
21 passed, 2 failed in 1.98s
```

## 6. Читання результатів параметризованих тестів

Після запуску такого тесту:

```python
@pytest.mark.parametrize("job, income", [
    ("IT",      50000),
    ("спорт",   20000),
    ("військо", 15000),
])
def test_job_risk(model, job, income):
    risk = model.predict_proba([[job, 30, income]])[0][1]
    assert risk >= 0
```

Результат буде виглядати так:

```
test_model.py::test_job_risk[IT-50000]       PASSED
test_model.py::test_job_risk[спорт-20000]    PASSED
test_model.py::test_job_risk[військо-15000]  FAILED
```

Одразу видно, **для якого конкретного набору параметрів** тест впав. Це дуже зручно при тестуванні різних категорій користувачів або сегментів даних.

## Практичний підхід
### Практичний шаблон для API тестів

Коли базові речі типу fixtures, requests/session та структура тестів уже знайомі, далі основний фокус переходить на архітектуру, підтримуваність і стабільність тестового фреймворку.

Для API тестів зазвичай потрібно продумати:

* як організувати API clients або service layer
* де зберігати endpoints
* як працювати з авторизацією та токенами
* як перевикористовувати common request logic
* як обробляти retries, timeouts та нестабільні сервіси
* як робити validation response schema
* як організувати test data
* як ізолювати тести між собою
* як запускати тести в різних environment (dev/stage/prod-like)

У хорошому API framework зазвичай є:

* окремий layer для HTTP-запитів
* utilities/helper methods
* конфігурація через env variables
* централізовані assertions
* логування request/response
* репорти
* CI/CD integration

Також важливо продумати:

* negative scenarios
* edge cases
* різні статус-коди
* partial/malformed responses
* rate limits
* performance aspects
* backward compatibility API

API тестування зазвичай більш стабільне, швидке та дешевше в підтримці, ніж UI.

### Відмінності для UI тестування

У UI тестуванні основна складність — не HTTP-рівень, а нестабільність інтерфейсу та взаємодія з браузером.

Навіть якщо вже використовується Page Object Model, потрібно окремо продумати:

* стабільні локатори
* waits/synchronization
* handling dynamic elements
* popups/modals/toasts
* flaky behavior
* browser compatibility
* responsive behavior
* screenshots/videos/logs
* parallel execution

У UI automation дуже важливо мінімізувати flaky tests.

Тому хороший UI framework зазвичай має:

* centralized waits
* base page abstraction
* reusable components
* helper methods
* retry logic для нестабільних дій
* automatic screenshots on failure
* reporting integration

Також UI тести часто потребують:

* тестових акаунтів
* cleanup після тестів
* preconditions setup
* mock/stub environments
* test isolation


### Головна різниця між API та UI тестами

API тести перевіряють бізнес-логіку і backend behavior напряму.

UI тести перевіряють:

* інтеграцію всіх шарів системи
* поведінку користувача
* frontend rendering
* browser interactions

Через це:

* API тести швидші
* API тести стабільніші
* API тести простіше дебажити
* UI тести дорожчі в підтримці
* UI тести більше схильні до flaky behavior

Тому в реальних проектах зазвичай будують test pyramid:

* багато API/unit тестів
* менше UI тестів
* UI покриває лише critical user flows

Це дозволяє отримати швидкий і стабільний feedback від automation suite.

## Підсумок

| Інструмент | Для чого |
|---|---|
| `@pytest.fixture` | підготувати модель або датасет один раз |
| `scope="session"` | не перенавчати модель перед кожним тестом |
| `conftest.py` | спільні фікстури для всього проєкту |
| `@pytest.mark.parametrize` | перевіряти одну логіку для багатьох значень |
| `@pytest.mark` | групувати тести за категоріями |
| `--html` | генерувати звіт для команди або замовника |

Ці інструменти дозволяють тестувати AI-системи **систематично**: перевіряти якість даних, поведінку моделі та наявність bias — не пишучи окремий тест для кожного випадку, а описуючи **правило** і перевіряючи його для всіх потрібних комбінацій.