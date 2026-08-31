# -*- coding: utf-8 -*-
# Самостійне вивчення методів list, tuple, set, dict
# Виконайте завдання та збережіть результати у вказаних змінних

print("=== РОБОТА З СПИСКАМИ (LIST) ===")

# Task 1. Створіть список з числами від 1 до 5
numbers = [0, 1, 2, 3, 4, 5]  # Ваш код тут

# Task 2. Додайте число 6 в кінець списку numbers

numbers.append(6)
print(numbers)

# Task 3. Вставте число 0 на початок списку numbers  
numbers.insert(0,0)
print(numbers)
# Task 4. Видаліть перше входження числа 3 зі списку numbers
numbers.remove(3)
print(numbers)

# Task 5. Знайдіть індекс елемента 'cherry' у списку fruits
fruits = ['apple', 'banana', 'cherry', 'banana', 'date']
cherry_index = fruits.index('cherry')
print(cherry_index)

# Task 6. Порахуйте кількість входжень 'banana' у списку fruits
banana_count = fruits.count('banana')
print(banana_count)

# Task 7. Відсортуйте список fruits за алфавітом
fruits.sort()
print(fruits)

# Task 8. Створіть копію списку fruits
fruits_copy = []  # Ваш код тут

print("\n=== РОБОТА З КОРТЕЖАМИ (TUPLE) ===")

# Task 9. Створіть кортеж з днями тижня
weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
  # Ваш код тут

# Task 10. Знайдіть індекс 'Wednesday' у кортежі weekdays
wednesday_index =  weekdays.index('Wednesday')
print(wednesday_index) # Ваш код тут

# Task 11. Порахуйте кількість входжень 'Monday' у кортежі
test_tuple = ('Monday', 'Tuesday', 'Monday', 'Friday', 'Monday')
monday_count = test_tuple.count("Monday")
print(monday_count)  # Ваш код тут

# Task 12. Перетворіть кортеж weekdays на список

weekdays_list = list(weekdays)  # Ваш код тут

print(weekdays_list)


print("\n=== РОБОТА З МНОЖИНАМИ (SET) ===")

# Task 13. Створіть множину з унікальних чисел
unique_numbers = {1,2,3,4,5}  # Ваш код тут: додайте числа 1, 2, 3, 4, 5

# Task 14. Додайте число 6 до множини unique_numbers
unique_numbers.add(6)
print(unique_numbers)

# Task 15. Видаліть число 3 з множини unique_numbers
unique_numbers.remove(3)
print(unique_numbers)

# Task 16. Створіть дві множини та знайдіть їх об'єднання
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
print(union_set)  # Ваш код тут

# Task 17. Знайдіть перетин множин set_a та set_b
intersection_set = set_a.intersection(set_b) 
print(intersection_set) # Ваш код тут

# Task 18. Знайдіть різницю set_a - set_b
difference_set = set_a.difference(set_b) 
print(difference_set) # Ваш код тут

# Task 19. Перевірте, чи є число 4 у множині unique_numbers
is_four_present = 4  # Ваш код тут

if is_four_present in unique_numbers:
    print(f"Елемент {is_four_present} присутній в множині.")

print("\n=== РОБОТА З СЛОВНИКАМИ (DICT) ===")

# Task 20. Створіть словник з інформацією про студента
student = dict(name= "John", age=25, cource=1)  # Ваш код тут: додайте ім'я, вік, група
print(student)

# Task 21. Додайте до словника student ключ 'grade' зі значенням 'A'
student["grade"] = "A"
print(student)

# Task 22. Отримайте значення ключа 'name' зі словника student
student_name = student["name"]
print(student_name) # Ваш код тут

# Task 23. Отримайте всі ключі словника student
student_keys =  student.keys()
print(student_keys) # Ваш код тут

# Task 24. Отримайте всі значення словника student  
student_values = student.values()  # Ваш код тут
print(student_values)

# Task 25. Видаліть ключ 'grade' зі словника student
del student['grade']
print(student)

# Task 26. Створіть словник з квадратами чисел від 1 до 5
squares_dict = {x: x**2 for x in range(6)}  # Ваш код тут: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares_dict)

# Task 27. Перевірте, чи існує ключ 3 у словнику squares_dict
#key_exists =   # Ваш код тут
print(3 in squares_dict)

# Task 28. Оновіть словник student новими даними
new_data = {'city': 'Kyiv', 'hobby': 'programming'}
student.update(new_data)
print(student)
if __name__ == "__main__":
    print("\n=== ЗАВЕРШЕННЯ ===")
    print("Всі завдання виконано! Запустіть test_selflearning.py для перевірки.")