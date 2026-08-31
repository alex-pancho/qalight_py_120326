# -*- coding: utf-8 -*-
"""
Завдання для самостійного вивчення: Функції в Python
===================================================

Це файл з завданнями для закріплення матеріалу про функції в Python.
Виконайте всі завдання послідовно. Перевірити правильність можна запустивши test_selflearning.py

Теми:
- Створення функцій
- Аргументи функцій
- *args і **kwargs
- Позиційні та ключові параметри
- Лямбда-функції
- Вбудовані функції (map, zip, isinstance, type, sort, sorted)
"""

# =============================================================================
# ЗАВДАННЯ 1: Основи створення функцій
# =============================================================================

def greeting(name):
    """
    Завдання 1.1: Створіть функцію, яка приймає ім'я та повертає привітання
    
    Args:
        name (str): Ім'я для привітання
        
    Returns:
        str: Рядок привітання у форматі "Привіт, {name}!"
    """
    # TODO: Реалізуйте функцію
    return f"Привіт, {name}!" 
print(greeting("Ivan"))

def calculate_area(length, width):
    """
    Завдання 1.2: Функція для обчислення площі прямокутника
    
    Args:
        length (float): Довжина прямокутника
        width (float): Ширина прямокутника
        
    Returns:
        float: Площа прямокутника
    """
    # TODO: Реалізуйте функцію
    return length * width
area = calculate_area(25, 15.65)
print(area)

def is_even(number):
    """
    Завдання 1.3: Перевірка чи число парне
    
    Args:
        number (int): Число для перевірки
        
    Returns:
        bool: True якщо число парне, False якщо непарне
    """
    # TODO: Реалізуйте функцію
    return number % 2 ==0
print(is_even(5))


# =============================================================================
# ЗАВДАННЯ 2: Функції з позиційними та ключовими аргументами
# =============================================================================

def create_profile(name, age, city="Не вказано", profession="Не вказано"):
    """
    Завдання 2.1: Створення профілю користувача
    
    Args:
        name (str): Ім'я користувача
        age (int): Вік користувача
        city (str, optional): Місто. За замовчуванням "Не вказано"
        profession (str, optional): Професія. За замовчуванням "Не вказано"
        
    Returns:
        dict: Словник з інформацією про користувача
    """
    # TODO: Поверніть словник з ключами: name, age, city, profession
    test_dict = {"name": name, "age": age, "city": city, "profession": profession}
    return test_dict
print(create_profile("Ann", 27, "Lviv", "manager"))


def calculate_price(base_price, discount=0, tax=0.2):
    """
    Завдання 2.2: Розрахунок фінальної ціни з урахуванням знижки та податку
    
    Args:
        base_price (float): Базова ціна
        discount (float, optional): Знижка (від 0 до 1). За замовчуванням 0
        tax (float, optional): Податок (від 0 до 1). За замовчуванням 0.2
        
    Returns:
        float: Фінальна ціна після знижки та податку
    """
    # TODO: Обчисліть фінальну ціну: (base_price * (1 - discount)) * (1 + tax)
    price = (base_price * (1 - discount)) * (1 + tax)
    return price
print(calculate_price(100.99, ))


# =============================================================================
# ЗАВДАННЯ 3: *args і **kwargs
# =============================================================================

def sum_all(*args):
    """
    Завдання 3.1: Функція для додавання будь-якої кількості чисел
    
    Args:
        *args: Будь-яка кількість чисел
        
    Returns:
        int/float: Сума всіх переданих чисел
    """
    # TODO: Поверніть суму всіх переданих аргументів
    return sum(args)  
print(sum_all(1, 2))

def create_student(**kwargs):
    """
    Завдання 3.2: Створення студента з довільними параметрами
    
    Args:
        **kwargs: Довільні параметри студента
        
    Returns:
        dict: Словник з обов'язковими ключами name, age та всіма переданими параметрами
    """
    # TODO: Поверніть словник з переданими параметрами
    # Якщо name або age не передані, встановіть їх за замовчуванням
    student = kwargs.copy()
    student.setdefault("name", "Unknown")
    student.setdefault("age", 0)
    return student
print(create_student(name="John", age=25, city="New York"))
print(create_student(city="London"))


def flexible_function(*args, **kwargs):
    """
    Завдання 3.3: Функція, яка приймає і позиційні, і ключові аргументи
    
    Args:
        *args: Позиційні аргументи
        **kwargs: Ключові аргументи
        
    Returns:
        tuple: Кортеж з двох елементів: (список args, словник kwargs)
    """
    # TODO: Поверніть кортеж (list(args), kwargs)
    return (list(args),kwargs)

# Приклад виклику функції
print(flexible_function(1, "hello", 3, name="John", age=25))


# =============================================================================
# ЗАВДАННЯ 4: Лямбда-функції
# =============================================================================

# Завдання 4.1: Створіть лямбда-функцію для піднесення числа до квадрату
square =  lambda x: x**2
print("піднесення числа до квадрату:", square(6))  # TODO: Замініть None на лямбда-функцію

# Завдання 4.2: Лямбда-функція для перевірки чи число більше 10
is_greater_than_10 = lambda y: y > 10  # TODO: Замініть None на лямбда-функцію
print(is_greater_than_10(15))


# Завдання 4.3: Лямбда-функція для об'єднання двох рядків
concatenate = lambda n, m: n + m 
 # TODO: Замініть None на лямбда-функцію,

print(concatenate([1,3,5], [1,8,7]))
print(concatenate("Two ", "Strings"))
# =============================================================================
# ЗАВДАННЯ 5: Робота з вбудованими функціями
# =============================================================================


def check_type_vs_isinstance(value, check_type):
    """
    Завдання 5.1: Порівняння type() та isinstance()
    
    Args:
        value: Значення для перевірки
        check_type: Тип для перевірки
        
    Returns:
        tuple: (результат type(), результат isinstance())
    """
    # TODO: Поверніть кортеж з результатами type(value) == check_type та isinstance(value, check_type)
    type_result = type(value) == check_type
    isinstance_result = isinstance(value, check_type)
    return (type_result, isinstance_result)
print(check_type_vs_isinstance(5, str))

def sort_vs_sorted_demo(numbers):
    """
    Завдання 5.2: Різниця між sort() та sorted()
    
    Args:
        numbers (list): Список чисел
        
    Returns:
        tuple: (оригінальний список після sort(), новий відсортований список)
    """
    # TODO: Застосуйте sort() до оригінального списку і поверніть його разом з sorted()
    list_for_sorted = sorted(numbers)
    list_for_sort = numbers.copy()
    list_for_sort.sort()
    return (list_for_sorted, list_for_sort)
given_numbers = [1, 6, 2, 9]

print(sort_vs_sorted_demo(given_numbers))


# =============================================================================
# ЗАВДАННЯ 6: Складніші завдання
# =============================================================================

def filter_and_process(data, filter_func, process_func):
    """
    Завдання 6.1: Фільтрація та обробка даних
    
    Args:
        data (list): Список даних
        filter_func (function): Функція для фільтрації
        process_func (function): Функція для обробки
        
    Returns:
        list: Список оброблених елементів, які пройшли фільтрацію
    """
    # TODO: Відфільтруйте дані та обробіть їх
   
    


def create_multiplier(factor):
    """
    Завдання 6.2: Функція, яка повертає функцію (замикання)
    
    Args:
        factor (int/float): Множник
        
    Returns:
        function: Функція, яка множить переданий аргумент на factor
    """
    # TODO: Поверніть функцію, яка множить аргумент на factor
    def multiplication(number):
        return factor * number
    return multiplication
output = create_multiplier(5)
print(output(6))


def advanced_calculator(*args, operation="sum", **kwargs):
    """
    Завдання 6.3: Розширений калькулятор
    
    Args:
        *args: Числа для обчислення
        operation (str): Операція ("sum", "multiply", "max", "min")
        **kwargs: Додаткові параметри
        
    Returns:
        float/int: Результат обчислення
    """
    if not args:
        return 0

    if operation == "sum":
        result = sum(args)
    
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
            
    elif operation == "max":
        result = max(args)
        
    elif operation == "min":
        result = min(args)
        
    else:
        raise ValueError(f"Операція '{operation}' не підтримується.")

   
    precision = kwargs.get("precision")
    if precision is not None:
        result = round(result, precision)

    return result
print(advanced_calculator(8, 6, 3, operation="max", ))
    # TODO: Реалізуйте калькулятор з різними операціями
    



# =============================================================================
# ПРИКЛАДИ ВИКОРИСТАННЯ (для розуміння)
# =============================================================================

if __name__ == "__main__":
    # Приклади використання функцій
    print("=== Приклади використання ===")
    
    # Після реалізації функцій, розкоментуйте код нижче:
    
    print(greeting("Олексій"))
    print(calculate_area(5, 3))
    print(is_even(4))
    
    profile = create_profile("Марія", 25, city="Київ")
    print(profile)
    
    print(sum_all(1, 2, 3, 4, 5))

    
    print("Реалізуйте всі функції та перевірте їх за допомогою test_selflearning.py")