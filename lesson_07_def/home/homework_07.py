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

def sort_buy_age_diapason(person_list:list[tuple]):
    """Return sorted dictionary with division buy age
        """

    new_dict = {}
    for name, age in person_list:
        start = (age // 10) * 10
        end = start + 9
        range = f"{start}-{end}"
        new_dict.setdefault(range, []).append(name)
    sorted_dict = dict(sorted(new_dict.items()))
    return sorted_dict

sorted_dict = sort_buy_age_diapason([('Alice', 25), ('Boby', 19), ('Charlie', 32),
            ('David', 28), ('Emma', 22), ('Frank', 45)])
print(sorted_dict)

# task 8

def password_valid_check(password):
    """Password valid check. Return True if password more then 8 symbols and
        False if password less then 8 symbols
        """

    if len(password) >= 8:
        return True
    else:
        return False

password_input = input("Введіть пароль: ")
is_password_valid = password_valid_check(password_input)
print(is_password_valid)

# task 9
def year_check(year : int):
    """Return True if input year is leap or False if input year is non-leap.
        """
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

year_input = int(input("Введіть рік: "))
is_year_leap = year_check(year_input)
print(is_year_leap)

# task 10
def golosni_count(text: str):
    """Return number of vowels in string.
        """
    vowels = "аеиіїоуюя"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

text_input = input("Введіть текст: ").lower()
calculate_vowels = golosni_count(text_input)
print(calculate_vowels)



"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""