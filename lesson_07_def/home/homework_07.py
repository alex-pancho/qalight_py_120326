# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        # десь тут помилка, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum(a, b):
    result = a + b 
    return result

print(sum(5, 5))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

numbers = [1, 2, 3, 4, 5]
print("Середнє арифметичне списку чисел:", average(numbers))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(string):
    reversed_string = string[::-1]
    return reversed_string

text = "Yevhen"
print(reverse_string(text))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words):
    return max(words, key=len)
    
word_list = ("apple", "banana", "pineapple", "blackberry")
print("Найдовше слово у списку:", longest_word(word_list))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
def calculator(num1, num2, operation):

    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    else:
        return "Невідома операція"

num1 = float(input("Введіть перше число: "))
operation = input("Введіть операцію (+ або - або *): ")
num2 = float(input("Введіть друге число: "))

result = calculator(num1, num2, operation)
print("Результат:", result)

# task 8
def check_password(password: str) -> bool:
    return len(password) >= 8

password = input("Введіть пароль: ")

if check_password(password):
    print("Пароль правильний")
else:
    print("Пароль неправильний")

# task 9
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Введіть рік: "))

if is_leap_year(year):
    print("Рік високосний")
else:
    print("Рік не високосний")

# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""
def even_squares(numbers: list) -> list:
    return [x**2 for x in numbers if x % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = even_squares(numbers)

print(result)