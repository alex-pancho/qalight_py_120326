# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помилка, а може не одна
        if  result > 25:
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
two_number_sum = lambda x,y : x+y
print(two_number_sum(2,5))


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_mean(incoming_list):
    list_sum=0
    for i in incoming_list:
        list_sum += i
    print(list_sum/len(incoming_list))
arithmetic_mean([1,2,3,4,5,6,7,8,9,10])
    
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def revers_string(incoming_string : str):
    return "".join(reversed(incoming_string))

print(revers_string("Test string"))
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word_in_list(incoming_list : list[str]):
    longest_word = ""
    for i in incoming_list:
        if len(i) > len(longest_word):
            longest_word = i
    return longest_word
print(longest_word_in_list(["aaaa","bbb","ccccccc","dddddddd"]))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, то -1, якщо другий рядок
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
# Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
def task_10():
    person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
    new_dict = {}

    for i in person_list:
        if 10 <= i[1] <= 19:
            if '10-19' not in new_dict:
                new_dict['10-19'] = []
            new_dict['10-19'].append(i[0])

        if 20 <= i[1] <= 29:
            if '20-29' not in new_dict:
                new_dict['20-29'] = []
            new_dict['20-29'].append(i[0])

        if 30 <= i[1] <= 39:
            if '30-39' not in new_dict:
                new_dict['30-39'] = []
            new_dict['30-39'].append(i[0])

        if 40 <= i[1] <= 49:
            if '40-49' not in new_dict:
                new_dict['40-49'] = []
            new_dict['40-49'].append(i[0])
    sorted_dict = dict(sorted(new_dict.items()))
    print(sorted_dict)
# task 8
def password_valid_check():
    passwor_input = input("Введіть пароль")
    if len(passwor_input) > 8:
        print("Символів має бути більше 8")
    else:
        print("Пароль прийнято")
# task 9
def calculator_plus_minus():
    num1 = float(input("Введіть перше число: "))
    operation = input("Введіть операцію (+, -, ): ")
    num2 = float(input("Введіть друге число: "))
    if operation == "+":
        print(f"{num1} + {num2} = {num1+num2}")
    elif operation == "-":
        print(f"{num1} - {num2} = {num1-num2}")
    else:
        print("Ви ввели неправельну операцію")
# task 10
def password_valid_check():
    passwor_input = input("Введіть пароль")
    if len(passwor_input) > 8:
        print("Символів має бути більше 8")
    else:
        print("Пароль прийнято")
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""

def year_check():
    year_input = int(input("Введіть рік"))
    if (year_input % 400 == 0) or (year_input % 4 == 0 and year_input % 100 != 0):
        print("Рік високосний")
    else:
        print("Рік не високосний")



def golosni_count():
    text = input("Введіть текст: ").lower()
    vowels = "аеиіїоуюя"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    print(f"Кількість голосних: {count}")