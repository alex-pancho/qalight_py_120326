# Вправа 1: Проста математика
print("\n=== ВПРАВА 1: Калькулятор ===")
print("Створіть простий калькулятор для двох чисел і двох дій")
print("Підтримувані операції: +, -")

# Початок реалізації:
num1 = float(input("Введіть перше число: "))
operation = input("Введіть операцію (+, -, ): ")
num2 = float(input("Введіть друге число: "))
if operation == "+":
   print ("Сума:", num1 + num2)
else:
   print ("Різниця:", num1 - num2)

# Вправа 2: Перевірка паролю
print("\n=== ВПРАВА 2: Перевірка паролю ===")
print("Створіть систему перевірки паролю")
print("Пароль повинен містити принаймні 8 символів")
while True:
    password = input("Введіть пароль (будь-які символи): ")
    if len(password) >= 8:
        print("Password accepted")
        break
    else:
        print("Try again, enter at least 8 symbols")

print("End")


# Вправа 3: Визначення високосного року
print("\n=== ВПРАВА 3: Високосний рік ===")
print("Рік є високосним, якщо:")
print("- Ділиться на 4 І не ділиться на 100")
print("- АБО ділиться на 400")
year_input = input("Введіть рік: ")

if year_input.isdigit():
    year = int(year_input)
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        print("Рік є високосним")
    else:
        print("Рік є не високосним")
else:
    print("Error")

# Вправа 4: Лічильник голосних
print("\n=== ВПРАВА 4: Лічильник голосних ===")
print("Підрахуйте кількість голосних у рядку")

text = input("Введіть текст: ").lower()
vowels = "аеиіїоуюя"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"Кількість голосних: {count}")


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
colour = input(("Введіть колір прибульця (green, yellow, red): ").lower().strip())
if colour == "green":
   print("гравець щойно заробив 5 балів")
elif colour == "yellow":
   print("гравець щойно заробив 10 балів")
elif colour == "red":
   print("гравець щойно заробив 15 балів")
else:
 print("Unknown colour, try again") 

# Вправа 6: Піцерія *
print("\n=== ВПРАВА 6: Начинки для піци (pizza_topping) ===")
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
while True:
    pizza_topping = input("Введіть начинку для піци: ").lower().strip()
    if pizza_topping == "quit":
        print("Your pizza is ready")
        break
    print(f"This filling will be added to your pizza — {pizza_topping}")
    



# Вправа 7: Зворотний порядок цифр
print("\n=== ВПРАВА 7: Зворотний порядок ===")
print("Виведіть цифри числа у зворотному порядку")
number = input("Введіть число: ")


reversed_number = number[::-1]

print(f"Число у зворотному порядку: {reversed_number}")




# Вправа 8: Пошук максимального числа
print("\n=== ВПРАВА 8: Пошук максимального ===")
print("Знайдіть найбільше число серед введених")
print("Введіть 0 для завершення")

max_number = None 

while True:
    num = int(input("Введіть число (0 для завершення): "))
    if num == 0:
        break
    if max_number is None or num > max_number:
        max_number = num
        print(f"Новий рекорд! Максимум тепер: {max_number}")
if max_number is None:
   print("Ви не ввели жодного числа, крім 0.")
else:
    print(f"\nНайбільше число серед введених: {max_number}")

# Вправа 9: Виключення зі списку
print("\n=== ВПРАВА 9: Виключення зі списку ===")
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]
for i in fruits:
    if i == "orange":
       # print("Break викликаний на i =", i)
        continue
    print('елементи списку, окрім "orange":', i)

# Вправа 10: Вираз в один рядок
print("\n=== ВПРАВА 10: Вираз з умовою в один рядок ===")
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
   if i % 2 == 0:
      print(f"Квадрат парних чисел: {i} дорівнює:", i ** 2)

#    result = ["Відповідь вставте сюди"]
# print(result)  #  [4, 16, 36, 64, 100]