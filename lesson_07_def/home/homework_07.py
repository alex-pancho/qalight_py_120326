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
        if  result > 25:
            print("Number is greater")# Enter the action to take if the result is greater than 25
            pass
        print("Multiplication table(3):", str(number) + "x" + str(multiplier) + "=" + str(result))

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
def add(n, m):
    return n + m

sum_nm = add(5, 3)
print("ADD", sum_nm)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def avarage(numbers):
    return sum(numbers)/len(numbers)
number_list = [1,2,6]
avarage_abc = avarage(number_list)
print("Avarage number:", avarage_abc)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def my_string(text):
    return text[::-1]
test_string = "Hello"
reversed_string = my_string(test_string)
print("Рядок  у зворотному порядку:", reversed_string)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def list_word(words):
    return max(words, key=len)
test_words = ["grape", "melon", "cucumber", "avocado"]
max_word = list_word(test_words)
print("Hайдовше слово у списку:", max_word)

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

print("\n=== ВПРАВА 4: Лічильник голосних ===")
print("Підрахуйте кількість голосних у рядку")

def count_vowels(text):
    vowels = "аеиіїоуюя"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

user_input = input("Введіть текст: ").lower()

result = count_vowels(user_input)
print(f"Кількість голосних у вашому тексті: {result}")

# task 8 Задано список чисел numbers, потрібно знайти список квадратів
# парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def get_even_squares(nums):
    return [x**2 for x in nums if x % 2 == 0]
result = get_even_squares(numbers)
print("Square numbers:", result)  


# task 9
def describe_person(name, age, subject="Unknown"): 
    print(f"{name} is {age} years old and favourite subject is {subject}.")

describe_person("Ann", 35, "Math")


# task 10 
def course_cost(hours, price):
    return hours*price
costs = course_cost(10, 500)
print("Course costs:", costs)

#"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
#перетворіть їх у 4 функції, що отримують значення та повертають результат.
#Обов'язково документуйте функції та дайте зрозумілі імена змінним.
#"""