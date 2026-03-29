# Вправа 1: Проста математика
print("\n=== ВПРАВА 1: Калькулятор ===")
print("Створіть простий калькулятор для двох чисел і двох дій")
print("Підтримувані операції: +, -")

# Початок реалізації:
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

#calculator_plus_minus()


    

# Вправа 2: Перевірка паролю
print("\n=== ВПРАВА 2: Перевірка паролю ===")
print("Створіть систему перевірки паролю")
print("Пароль повинен містити принаймні 8 символів")

def password_valid_check():
    passwor_input = input("Введіть пароль")
    if len(passwor_input) > 8:
        print("Символів має бути більше 8")
    else:
        print("Пароль прийнято")

#password_valid_check()



# Вправа 3: Визначення високосного року
print("\n=== ВПРАВА 3: Високосний рік ===")
print("Рік є високосним, якщо:")
print("- Ділиться на 4 І не ділиться на 100")
print("- АБО ділиться на 400")

def year_check():
    year_input = int(input("Введіть рік"))
    if (year_input % 400 == 0) or (year_input % 4 == 0 and year_input % 100 != 0):
        print("Рік високосний")
    else:
        print("Рік не високосний")

#year_check()

# Вправа 4: Лічильник голосних
print("\n=== ВПРАВА 4: Лічильник голосних ===")
print("Підрахуйте кількість голосних у рядку")



# код тут
def golosni_count():
    text = input("Введіть текст: ").lower()
    vowels = "аеиіїоуюя"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    print(f"Кількість голосних: {count}")

#golosni_count()
    

# Вправа 5: Гра 
print("\n=== ВПРАВА 5: Гра ===")
"""
Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо колір прибульця green, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця yellow, надрукуйте, що гравець щойно заробив 10 балів.
Якщо колір прибульця red - надрукуйте, що гравець щойно заробив 15 балів.
Перевірте роботу гри самостійно, змінюючи значення alien_color
"""
def alien_game():
    alien_color = int(input("Виберіть колір цифрою від 1 до 3: 1 --> green, 2 --> yellow, 3 --> red :  "))

    if alien_color == 1:
        alien_color = "green"
    elif alien_color == 2:
        alien_color = "yellow"
    elif alien_color == 3:
        alien_color = "red"
    else:
        print("Ви ввели неправельну цифру. Гра завершена!")
        return

    if alien_color == "green":
        print("Ви заробили 5 балів")
    elif alien_color == "yellow":
        print("Ви заробили 10 балів")
    elif alien_color == "red":
        print("Ви заробили 15 балів")

#alien_game()



# Вправа 6: Піцерія *
print("\n=== ВПРАВА 6: Начинки для піци (pizza_topping) ===")
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""

def pizza_topping():
    quit_word = "quit"
    topping = ""
    while topping != quit_word:
        topping = input("Введіть назву начинки: ")
        print(f"Ми додамо {topping} до вашої піцци")

#pizza_topping()

# Вправа 7: Зворотний порядок цифр
print("\n=== ВПРАВА 7: Зворотний порядок ===")
print("Виведіть цифри числа у зворотному порядку")

def revert_number():
    number_input = input("Введіть число: ")
    for i in range(1,len(number_input)+1):
        print(number_input[-i], end="")
#revert_number()

# Вправа 8: Пошук максимального числа
print("\n=== ВПРАВА 8: Пошук максимального ===")
print("Знайдіть найбільше число серед введених")
print("Введіть 0 для завершення")
def find_max_number():
    stop_number = 0
    list_numbers = []
    number_input = None
    while number_input != stop_number:
        number_input = int(input("Введіть число: "))
        list_numbers.append(number_input)
    current_number = 0
    max_number = 0
    for i in range(len(list_numbers)):
        current_number = list_numbers[i]
        if current_number > max_number:
            max_number = current_number
        else:
            continue
    print(f"Найбільше число: {max_number}")
find_max_number()
    

# Вправа 9: Виключення зі списку
print("\n=== ВПРАВА 9: Виключення зі списку ===")
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]
for i in range(len(fruits)):
    if fruits[i] == "orange":
        continue
    print(fruits[i])



# Вправа 10: Вираз в один рядок
print("\n=== ВПРАВА 10: Вираз з умовою в один рядок ===")
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        result.append(numbers[i]**2)
    else:
        continue

print(result)  #  [4, 16, 36, 64, 100]
